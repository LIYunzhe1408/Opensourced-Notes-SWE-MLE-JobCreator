## Introduction
Hi xx, I'm Jonas, a master student in EECS from UC Berkeley. My interest is computer vision and machine learning within Robotics and 
autonomous vehicles. Over the past 7 years, as a team lead and a computer vision engineer, I’ve developed computer vision systems for mobile robots, 
working under real-time and complex scenarios.  Besides that, I have conducted research using machine learning in field of battery and computer vision 
explanability, these are two parts also important to make a decision and choose a energy source for a intelligent agent. Before graduation from undergrad, 
based on my combination background of technology and team lead experience, I got a position as a product manager in Momenta. I really like every moment creating 
robots and programs with my team and bring innovative ideas to the real world. The position as a perception sw engineer at xxx exactly align with my interest and 
career plan, so I think it would be a great fit into this position.

## DJI RoboMaster Competition
Director of a 40-student team to build 8 types of robots from scratch to product
* Camera: Industrial Camera, Camera Model, MatLab Calibrator, Rigid Body Motion
* OpenCV: Pre-process video input, data augmentation
* Object Detection: YOLO series models, related work(RCNN, SSD, ...)
* Machine Learning Metric: Precision, Recall, F-1 (https://blog.csdn.net/lhxez6868/article/details/108150777)
* Object Tracking: Kalman Filter, Least Square
* Linux/C++: Digital Twin Framework(our system exactly reflects physical environment), Serial Communication with micro controller(i.e. STM32), environment setup
* BQ story:  
  1. Implement object detection in OpenCV rather than DNN
  2. A bad decision for drone
  3. Conflict about priority of CV or Stability

## Visual Explainer For Deep Learning Decisions
Developed a web application for explaining DNN image classification decisions.
> Yunzhe Li. Design and implementation of a research platform for interpretation of deep learning decision results in line with human cognition[D]. Shanghai: Shanghai University, 2024
![Yunzhe Li. Design and implementation of a research platform for interpretation of deep learning decision results in line with human cognition[D]. Shanghai: Shanghai University, 2024](./HCE%20Architecture.png)
* Image Segmentation: Semantic Segmentation(assign a category for each pixel, DeepLabv3, FCN, ...), Superpixel Segmentation
* AutoEncoder: Encode constraints to construct a tree structure
* Clustering Algorithm
* Full stack development: Vue.js for frontend, Django for backend, MySQL for database

## Mining Property Relations of NASICON Solid Electrolyte
Developed a web application for investigating relations between material properties
* Data Labeling
* NER: MatBERT-BiLSTM-CRF
* RE: MatBERT-BiGRU-Softmax
* Knowledge Graph: Py2Neo
* Full stack development: Vue.js for frontend, SpringBoot for backend, MySQL for database

## Momenta
Product management of autopilot software for GM Cadillac in challenging underground parking scenarios
* PyDocx: Automate simulation data processing
* Overview of autonomous vehicle pipeline
* BQ stories:
  1. Negotiating the goals and deliverables with the client.
  2. Automate the delivery of simulation reports