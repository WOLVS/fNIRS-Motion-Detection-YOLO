# fNIRS-Motion-Detection-YOLO
Edge Implementation based on PYNQ-Z2

--------------------------------------------------------------------
Team number: AOHW25-604
Project name: Edge Implementation of Artificial Neural Network for fNIRS applications
Link to YouTube Video(s): https://youtu.be/5Mxn1vnKkiQ
Link to project repository: https://github.com/WOLVS/fNIRS-Motion-Detection-YOLO.git
--------------------------------------------------------------------

University name: University of Leeds

Participant(s): 
  Participant 1: Yunyi Zhao
  Email: yunyi.zhao.21@ucl.ac.uk

  Participant 2: Xinchen Zhou
  Email: dtqk4464@leeds.ac.uk
  
Supervisor name: Dr Shufan Yang
Supervisor e-mail: s.yang@napier.ac.uk
--------------------------------------------------------------------

Board used: PYNQ-Z2
Software Version: MobaXterm
                  DNNDK v3.1

Brief description of project: 
This project builds an edge intelligence prototype on the PYNQ-Z2 and integrates it with YOLOv3 object detection on the board to dynamically adjust detection and interaction strategies. The system uses the official DPU to accelerate YOLOv3 inference, achieving real-time, low-power object detection.

--------------------------------------------------------------------
Description of archive:

Directory structure:
- /Compile_Tools: Contains scripts for quantizing the model, kernel compilation, and cross-compilation
- /pre_trained_model: Contains the TensorFlow YoloV3 model with anchors and classes configuration
- /tf_yolov3_motion_deploy: Contains the testing files for on-board execution

Source files:
- /Compile_Tools: Various scripts to prepare the model for deployment
- /pre_trained_model: The TensorFlow YoloV3 model files
- /tf_yolov3_motion_deploy/libdpumodeltf_yolov3_motion.so: The compiled DPU kernel dynamic link library
- /tf_yolov3_motion_deploy/tf_yolov3_voc_pic_V1.py: The testing Python script
--------------------------------------------------------------------

Instructions to build project on PYNQ-Z2:

Step 1: Download and burn the image file to SD card (https://drive.google.com/file/d/1YQ_bBGqo_Cpm5JArbu0bOplzQ293TBn9/view), launch and initialize the PYNQ-Z2 board.
Step 2: Drag the YOLO_V3 file to the work space in MobaXterm and enter the work file(on board).
Step 3: Run 'Make' commmand to use the Malefile document to build a yolo_image executable program (on board).
Step 4: Run 'yolo_image' program and select the specific image. The YOLO detection will be started.

--------------------------------------------------------------------
