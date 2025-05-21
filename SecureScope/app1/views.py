from django.shortcuts import render, redirect
import pyrebase
from django.conf import settings
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import numpy as np
import face_recognition
from PIL import Image
import os
import pickle
import numpy as np
from .forms import PersonForm
from django.http import StreamingHttpResponse
from django.views.decorators.gzip import gzip_page
import cv2
import face_recognition
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from .models import FaceRecord
import datetime
from deepface import DeepFace

# Initialize Firebase
config = {
    'apiKey': settings.FIREBASE_API_KEY,
    'authDomain': settings.FIREBASE_AUTH_DOMAIN,
    'databaseURL': settings.FIREBASE_DATABASE_URL,
    'projectId': settings.FIREBASE_PROJECT_ID,
    'storageBucket': settings.FIREBASE_STORAGE_BUCKET,
    'messagingSenderId': settings.FIREBASE_MESSAGING_SENDER_ID,
    'appId': settings.FIREBASE_APP_ID,
    'measurementId': settings.FIREBASE_MEASUREMENT_ID
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def index(request):
    
    return render(request, "index.html")

# Load existing encodings if available
ENCODINGS_FILE = "face_encodings.pkl"
if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, "rb") as f:
        known_face_encodings, known_face_names = pickle.load(f)
else:
    known_face_encodings = []
    known_face_names = []

def register_face(image, name,additional_info):
    try:
        print("registering")

        if image is None:
            return "No image provided. Please upload an image."

        # Convert image to RGB format if not already
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Convert image to numpy array
        image_np = np.array(image)

        # Detect face encodings
        face_encodings = face_recognition.face_encodings(image_np)
        if len(face_encodings) == 0:
            return "No face detected. Please try again."

        face_encoding = face_encodings[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)

        # Save the face encodings to file
        save_face_encodings()
        
        # Convert PIL image to a Django-friendly file
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        file_name = f'{name}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
        image_file = ContentFile(buffer.getvalue(), file_name)
        print('Done')
        # Save to database
        
        face_record = FaceRecord(image=image_file, name=name,additional_info=additional_info)
        face_record.save()
    except Exception as e:
        print(e)
    print('done')
    return f"Face registered for {name}."

def save_face_encodings():
    # Save the face encodings to file
    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump((known_face_encodings, known_face_names), f)


def recognize_face(image):
    if image is None:
        return "No image provided."

    # Convert image to RGB format if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Convert image to numpy array
    image_np = np.array(image)

    # Detect face locations and encodings
    face_locations = face_recognition.face_locations(image_np)
    if len(face_locations) == 0:
        return "No face detected."

    face_encoding = face_recognition.face_encodings(image_np, face_locations)[0]
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    
    if face_distances.size == 0:  # If face_distances is empty
        
        return "Unknown"

    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
    else:
        name = "Unknown"
        
    return name


import numpy as np

def register_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
            
            name = ''
            face_detected = False
            while not face_detected:
                # Detect face locations
                face_locations = face_recognition.face_locations(rgb_frame)
                
                if face_locations:
                    # If face detected, recognize and analyze
                    face_image = frame[face_locations[0][0]:face_locations[0][2], face_locations[0][3]:face_locations[0][1]]
                    pil_image = Image.fromarray(face_image)
                    name = recognize_face(pil_image)
                    
                    if name == 'Unknown' or name=='No face detected.':
                        try:
                            # Convert PIL Image to numpy array
                            np_image = np.array(pil_image)
                            
                            # Analyze using DeepFace
                            analysis = DeepFace.analyze(np_image, actions=['age', 'gender', 'race'], enforce_detection=False)
                            data={form.cleaned_data['name']:analysis}
                            database.child('Data').push(data)
                            additional_info=analysis
                        except Exception as e:
                            print(e)
                            additional_info = " Analysis Error"
                            continue  # Skip current frame and try again
                        
                        register_face(pil_image, form.cleaned_data['name'], additional_info)
                        face_detected = True  # Exit loop after successful registration
                    else:
                        cap.release()
                        error_message = f"Face already exists for {name}. Please try again."
                        form = PersonForm()
                        return render(request, 'register_person.html', {'form': form, 'error_message': error_message})
                
                # If no face detected, continue capturing frames
                ret, frame = cap.read()
                rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
            
            # Save the form after successful registration
            form.save()
            cap.release()
            return redirect('index')
    else:
        form = PersonForm()
    
    return render(request, 'register_person.html', {'form': form})



def success(request):
    return render(request, 'success.html')

@gzip.gzip_page
def face_tracking(request):
    cap = cv2.VideoCapture(0)

    def detect_faces(frame):
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
        face_locations = face_recognition.face_locations(rgb_frame)

        for (top, right, bottom, left) in face_locations:
            face_image = frame[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            name = recognize_face(pil_image)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom), (right, bottom + 35), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom + 28), font, 1.0, (255, 255, 255), 1)

        return frame

    def stream():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_with_faces = detect_faces(frame)
            _, jpeg = cv2.imencode('.jpg', frame_with_faces)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
