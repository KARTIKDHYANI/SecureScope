
# 🛡️ SecureScope

**SecureScope** is a real-time facial recognition and demographic analysis system designed for modern surveillance and security applications. It combines deep learning, computer vision, and secure data management to provide accurate identification while respecting privacy and ethical considerations.

---

## 📌 Features

* 🎯 **Real-Time Facial Recognition**: High-accuracy detection using deep learning.
* 👥 **Demographic Analysis**: Age, gender, and ethnicity prediction with deep models.
* 🧠 **Pickle-Based Encoding Storage**: Facial features are stored as serialized `.pkl` embeddings for fast recognition.
* 🔐 **Secure & Ethical Surveillance**: Access control, data encryption, and privacy-first design.
* 🗃️ **SQLite Storage**: Lightweight local database for quick access.
* ☁️ **Firebase Backup**: Ensures secure cloud-based redundancy and real-time sync.
* 🖥️ **Web-Based Interface**: Built with Django for ease of use and admin control.
* 📡 **Live Monitoring**: Real-time face recognition from video streams.

---

## 🧱 Architecture Overview

| Component            | Role                                                        |
| -------------------- | ----------------------------------------------------------- |
| **OpenCV**           | Real-time video/image capture and preprocessing             |
| **Face Recognition** | Facial embedding extraction and comparison                  |
| **DeepFace**         | Demographic analysis (age, gender, ethnicity)               |
| **Dlib**             | Face detection and alignment                                |
| **TensorFlow**       | Deep learning model training and adaptation                 |
| **Firebase**         | Cloud-based backup and real-time database                   |
| **SQLite**           | Local database for storing metadata                         |
| **Pickle**           | Facial encodings stored in `.pkl` format for fast retrieval |
| **Django**           | Backend framework and admin interface                       |

---

## 🔄 Workflow

1. **Face Detection** – Detect faces in live video using OpenCV + Dlib.
2. **Face Alignment** – Standardize face orientation to improve recognition accuracy.
3. **Feature Extraction** – Extract facial embeddings using Face Recognition.
4. **Encoding and Storage** – Save face embeddings as `.pkl` files locally.
5. **Demographic Profiling** – Analyze age, gender, and race using DeepFace.
6. **Verification** – Match new faces with stored encodings and display results.
7. **Backup** – Periodic sync of metadata and logs to Firebase.

---

## 📷 Applications

* **Public Surveillance**: Airports, metro stations, stadiums
* **Retail Analytics**: Customer demographic analysis and behavior tracking
* **Law Enforcement**: Real-time suspect tracking and investigation
* **Smart Access Control**: Employee verification and facility security
* **Home Security**: Personalized access and intrusion detection

---

## 🧪 Tech Stack

* **Frontend**: HTML/CSS, JavaScript
* **Backend**: Django (Python)
* **Core Libraries**: OpenCV, Dlib, Face Recognition, DeepFace, TensorFlow
* **Storage**:

  * **SQLite** for fast, local data handling
  * **Firebase** for cloud-based backups and real-time sync
  * **Pickle (`.pkl`)** for efficient facial embedding storage
* **Deployment**: Docker (optional for consistency)

---

## 🛠️ How to Run

To get started with **SecureScope**, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/KARTIKDHYANI/SecureScope.git

# 2. Navigate to the project directory
cd SecureScope

# 3. Create a virtual environment
python -m venv env

# 4. Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# 5. Install required dependencies
pip install -r requirements.txt

# 6. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 7. Start the Django development server
python manage.py runserver
```

Once the server is running, open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the application.





---


## 🖥️ Application Interface

<p align="center">
  <img width="1439" alt="SecureScope Dashboard" src="https://github.com/user-attachments/assets/e5cb6f90-daf3-4e48-9337-cb84182bd1c5" />
  <br>
  <em>Figure 1: SecureScope dashboard showing real-time face detection on initial launch</em>
</p>

<p align="center">
  <img width="1437" alt="Face Registration Page" src="https://github.com/user-attachments/assets/8d11090c-b14c-44ec-b732-aec52b294705" />
  <br>
  <em>Figure 2: Interface to register an unknown person into the system</em>
</p>

<p align="center">
  <img width="1440" alt="Registered User Details" src="https://github.com/user-attachments/assets/afd73111-e87c-4722-875a-e44285c79e67" />
  <br>
  <em>Figure 3: Stored facial features and metadata of the registered person</em>
</p>

<p align="center">
  <img width="1440" alt="Recognition Success" src="https://github.com/user-attachments/assets/efc66580-e771-4d04-9261-60f1a86d5caa" />
  <br>
  <em>Figure 4: SecureScope recognizing the registered person using updated encodings</em>
</p>

<p align="center">
  <img width="1082" alt="Firebase JSON Structure" src="https://github.com/user-attachments/assets/32a56c52-b690-40a4-808e-32f31913003d" />
  <br>
  <em>Figure 5: JSON structure in Firebase showing demographic and age details used for backup</em>
</p>



---


## 📈 Performance Highlights

* ✔️ **Recognition Accuracy**: 95%+ in diverse lighting and conditions
* ⚡ **Processing Speed**: \~30 FPS with GPU acceleration
* ☁️ **Backup Reliability**: Firebase ensures cloud recovery and remote access
* 🧠 **Low Latency Retrieval**: Instant encoding match via pickle-based structure

---

## 🚀 Future Enhancements

* Integration with IoT surveillance devices
* Gesture and behavior tracking using OpenPose
* Auto-deployment using Docker + CI/CD
* Expanded multi-face tracking and heatmap visualizations

---

## 📚 References

* [OpenCV](https://opencv.org/)
* [Face Recognition](https://github.com/ageitgey/face_recognition)
* [DeepFace](https://github.com/serengil/deepface)
* [TensorFlow](https://www.tensorflow.org/)
* [Dlib](http://dlib.net/)
* [Firebase](https://firebase.google.com/)


