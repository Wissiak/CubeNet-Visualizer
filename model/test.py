from ultralytics import YOLO

model = YOLO('/opt/homebrew/runs/detect/train2/weights/last.pt')

#model(source="input.mp4", show=True, conf=0.1, save=True, device='mps')
results = model("wurfelnetz-2/test/images/Screenshot-2024-02-05-at-19-24-43_png.rf.87dfa6c72a0fe50a6a5fff309f3134e4.jpg", conf=0.6)

print(results)


from PIL import Image

r = results[0]
im_array = r.plot()  # plot a BGR numpy array of predictions
im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
im.show()

'''
from roboflow import Roboflow
rf = Roboflow(api_key="9wREGGZo08MwxlGSJan0")
project = rf.workspace().project("wurfelnetz")

model = project.version(2).model

#model(source="input.mp4", show=True, conf=0.1, save=True, device='mps')
results = model.predict("model/test2.png", confidence=40, overlap=30).json()

print(results)
'''