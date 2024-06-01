# views.py

from django.shortcuts import render
import pyrebase
from django.conf import settings

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

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

# Create your views here.
def index(request):
    try:
        name = database.child('Data').child("Name").get().val()
    except Exception as e:
        name = None
        print(f"An error occurred: {e}")
    
    return render(request, "index.html", {"name": name})
