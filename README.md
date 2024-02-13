# Project: Object Tracking and Detection
This project aims to implement object tracking and detection algorithms using computer vision techniques. 
It provides tools to track and detect objects in images and video streams, facilitating various applications such as surveillance, augmented reality, and autonomous driving.

## Features:
Object Detection: Utilize state-of-the-art object detection models to identify and locate objects within images and video frames.
Object Tracking: Implement tracking algorithms to follow objects across consecutive frames in a video stream.
Multiple Object Support: Detect and track multiple objects simultaneously, enabling the monitoring of various entities in a scene.
Real-time Processing: Optimize algorithms for real-time performance, allowing for efficient object tracking and detection in live video feeds.
Customization: Easily customize and extend the project with new detection models, tracking algorithms, or integration with other libraries and frameworks.

## Setup the LOCAL GPU

1. Check GPU Compute Capability [here](https://developer.nvidia.com/cuda-gpus).

2. Install GPU driver from [NVIDIA](https://www.nvidia.com/download/index.aspx?lang=en-us).

3. Install CUDA Toolkits from [NVIDIA](https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Windows&target_arch=x86_64).

4. Download and Setup cuDNN from [NVIDIA](https://developer.nvidia.com/rdp/cudnn-archive):
   - You should find three folders: bin, include, lib.
   - Copy these folders and paste them into `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0`.

## YOLO to TensorFlow Converter

1. Download the ZIP file from [here](https://github.com/theAIGuysCode/yolov3_deepsort#command-line-args-reference).
2. Download and Save weight files:
   - [yolov3](https://pjreddie.com/media/files/yolov3.weights)
   - [yolov3-tiny](https://pjreddie.com/media/files/yolov3-tiny.weights).
3. Save weights files into the `weights` folder.

## Run the Project

1. Execute `convert.py` in terminal:
   ```bash
   python convert.py
   ```

2. Run main file
   ```bash
   python object_tracker.py
   ```
