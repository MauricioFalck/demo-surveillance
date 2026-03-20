import time

import cv2
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

cap = cv2.VideoCapture(0)

last_processed_time = 0
interval = 1.0

print("Processing one frame every second. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    if current_time - last_processed_time >= interval:
        last_processed_time = current_time

        results = model(frame, classes=[0, 67], verbose=False)

        person_count = len(results[0].boxes)
        detected_ids = results[0].boxes.cls.tolist()

        print(f"People: {person_count}")

        annotated_frame = results[0].plot()
        cv2.imshow("Person Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()
