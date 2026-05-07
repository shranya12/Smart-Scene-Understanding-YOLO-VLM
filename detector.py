from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")


def detect_objects(frame):
    results = model(frame)

    detected_objects = []

    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                detected_objects.append(label)

    return list(set(detected_objects))
