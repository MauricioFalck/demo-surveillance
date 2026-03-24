import time

import cv2
from ultralytics import YOLO

start_time = time.time()
last_processed_time = 0
interval = 3.0
person_count = 0
mobile_count = 0
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
            # COCO classes: 0 = person, 67 = cell phone.
            results = model(frame, classes=[0, 67], verbose=False)
            person_count = 0
            mobile_count = 0
            for box in results[0].boxes:
                class_id = int(box.cls.item())
                if class_id == 0:
                    person_count += 1
                elif class_id == 67:
                    mobile_count += 1
            print(f"People: {person_count} | Mobiles: {mobile_count}")

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
    cv2.putText(
        display_frame,
        f"Mobiles: {mobile_count}",
        (10, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.imshow("People and Mobile Detection", display_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
