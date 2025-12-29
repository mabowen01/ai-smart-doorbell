
# ai-smart-doorbell
# 🔔 AI Smart Doorbell

An AI-powered smart doorbell system that detects human faces using a webcam and rings a bell automatically.

Built with **Python**, **OpenCV**, and **face_recognition**.

---

## ✨ Features
- 📷 Real-time webcam face detection
- 🔔 Rings doorbell sound when a face is detected
- ⚡ Fast detection using frame resizing
- 🧵 Non-blocking audio with threading
- 🍎 Optimized for macOS (M1/M2)

---

## 🛠️ Technologies Used
- Python 3.11
- OpenCV
- face_recognition (dlib)
- macOS `afplay` for audio

---

## 📂 Project Structure

AI Doorbell/
│── main.py
│── Ding-dong.wav
│── README.md
│── .gitignore

---

## ⚙️ Installation (macOS)

### 1️⃣ Install Python 3.11
,,,bash
brew install python@3.11
2️⃣ Create virtual environment
python3.11 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install opencv-python face_recognition
⛔ Stop the Program
	•	Press q in the camera window
	•	Or press Ctrl + C in terminal
