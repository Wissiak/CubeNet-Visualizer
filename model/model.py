from ultralytics import YOLO

model = YOLO('yolov8n-obb.pt')

results = model.train(data=f"./dataset/data.yaml", epochs=10, imgsz=640, device='mps')