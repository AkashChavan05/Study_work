from ultralytics import RTDETR

# Load a COCO-pretrained RT-DETR-l model
model = RTDETR("rtdetr-l.pt")

# Display model information (optional)
model.info()

# run the inference on a video
results = model(
    "/home/fx/Desktop/Logical_Test/Ahmedabad_traffic.mp4",
    show=True,
    save=True,
)
