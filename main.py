import time

import cv2
from ultralytics import YOLO

start_time = time.time()
last_processed_time = 0
interval = 3.0
person_count = 0
grace_period = 5.0

model = YOLO("yolo26n.pt")
cap = cv2.VideoCapture(index=0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    current_time = time.time()

    if not current_time - start_time < grace_period:
        if current_time - last_processed_time >= interval:
            last_processed_time = current_time
            results = model(frame, classes=[0], verbose=False)
            person_count = len(results[0].boxes)
            print(f"People: {person_count}")

    display_frame = frame.copy()
    cv2.putText(
        display_frame,
        f"People: {person_count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("Person Detection", display_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
