import cv2
import os

# Webcam Setup
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

# Load Haarcascade
cascade_path = os.path.join("engine", "auth", "haarcascade_frontalface_default.xml")
if not os.path.exists(cascade_path):
    print("❌ Haarcascade file not found!")
    exit()

detector = cv2.CascadeClassifier(cascade_path)

# Create samples directory if it doesn't exist
samples_dir = os.path.join("engine", "auth", "samples")
os.makedirs(samples_dir, exist_ok=True)

# User Input
face_id = input("Enter a numeric user ID: ")
print("Taking samples, look at the camera...")

count = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Save face image
        face_img = gray[y:y + h, x:x + w]
        file_path = os.path.join(samples_dir, f"face.{face_id}.{count}.jpg")
        cv2.imwrite(file_path, face_img)

        # Show video with rectangle
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:  # ESC to quit
        break
    elif count >= 100:
        break

print("✅ Samples taken successfully. Exiting...")
cam.release()
cv2.destroyAllWindows()
