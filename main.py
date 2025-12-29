import cv2
import face_recognition
import threading
import os

cap = cv2.VideoCapture(0)
sound_played = False

def ring_bell():
    os.system("afplay Ding-dong.wav")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    # Resize for speed
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # BGR → RGB
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Face detection
    faces = face_recognition.face_locations(rgb_small_frame)

    if faces and not sound_played:
        threading.Thread(target=ring_bell, daemon=True).start()
        sound_played = True

    if not faces:
        sound_played = False

    cv2.imshow("Smart Doorbell", frame)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()