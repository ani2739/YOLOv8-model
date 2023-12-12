

# YOLOv8 INSTALLATION COMMAND 
# Pip install method (recommended)
%cd yolov8
!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

# FOR DATASET OF THE ROBOFLOW PUT HERE
!mkdir {HOME}/datasets
%cd {HOME}/datasets

# robolfow dataset
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="BUQIxo9xwUYVHrkPx9Ik")
project = rf.workspace("nirma-university-1bjp1").project("demo_of_potholes")
dataset = project.version(8).download("yolov8")

# model training 
!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/content/demo_of_potholes-8/data.yaml epochs=25 imgsz=800 plots=True

# model detection 
!yolo task=detect mode=predict model={demo_of_potholes}/runs/detect/train/weights/best.pt conf=0.25 source={dataset.location}/test/images save=True


