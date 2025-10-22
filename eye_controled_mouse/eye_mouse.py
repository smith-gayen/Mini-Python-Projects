import cv2
import pyautogui

cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Smoothing variables
prev_x, prev_y = None, None
alpha = 0.2  # Smoothing factor (0.1-0.3 recommended)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eye_center_x = x + ex + ew // 2
            eye_center_y = y + ey + eh // 2
            cv2.circle(frame, (eye_center_x, eye_center_y), 10, (0,255,0), 2)
            screen_x = screen_w * eye_center_x / frame.shape[1]
            screen_y = screen_h * eye_center_y / frame.shape[0]

            # Smoothing
            if prev_x is not None and prev_y is not None:
                screen_x = prev_x + alpha * (screen_x - prev_x)
                screen_y = prev_y + alpha * (screen_y - prev_y)
            prev_x, prev_y = screen_x, screen_y

            pyautogui.moveTo(screen_x, screen_y)
            break  # Move to first detected eye only

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()