from ultralytics import YOLO

model = YOLO('yolov8n-obb.pt')
name = "train-10"

results = model.train(
    data=f"./dataset/data.yaml", 
    epochs=10, 
    imgsz=640, 
    device='mps', 
    batch=64, 
    save_period=10, 
    dropout=0.3, 
    weights='yolov8n-obb.pt', 
    project='/Users/patrick/projects/digicamp/runs/obb', 
    name=name, 
    cache=True, 
    verbose=True, 
    workers=16
)