# fNIRS-Motion-Detection-YOLO
A prototype of fNIRS-Notion-Detection based on YOLO

--------------------------------------------------------------------
Team number: xohw23-138
Project name: FPGA-Based Prototype: A Neural Network Implementation for Real-Time Motion Artifact Detection in Wearable fNIRS System
Link to YouTube Video(s): https://youtu.be/LLHI3ttyQKA
Link to project repository: https://github.com/WOLVS/fNIRS-Motion-Detection-YOLO.git
--------------------------------------------------------------------

University name: University College London

Participant(s): 
  Participant 1: Yunyi Zhao
  Email: yunyi.zhao.21@ucl.ac.uk

  Participant 2: Yunjia Xia
  Email: Yunjia.xia.18@ucl.ac.uk
  
Supervisor name: Dr Shufan Yang
Supervisor e-mail: s.yang@napier.ac.uk
--------------------------------------------------------------------

Board used: AXU3EG
Software Version: Vitis-ai 1.2.0

Brief description of project: 
This project presents the creation and development of an innovative FPGA-based prototype for real-time, low-power detection of motion artifacts in a wearable functional near-infrared spectroscopy (fNIRS) system. It outlines the process of developing the design for a standalone FPGA platform employing a neural network for motion artifact detection and elucidates the method of evaluating the removal of these motion artifacts.

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

Instructions to build project (you don't need to build the project for testing):

Step 1: Download and boot "xilinx/vitis-ai:1.2.82" Docker.
Step 2: Run "conda activate vitis-ai-tensorflow" to enter the TensorFlow environment.
Step 3: Run "source 1_tf_quantize.sh" and "source 2_vai_compile.sh".
Step 4: Exit this docker and download & boot "xilinx/vitis-ai:runtime-1.0.0-cpu" docker and run "source 3_lib_compiler_runtime.sh". After these steps, you should get ".so" dll file for DPU.

Instructions to test project:

Step 1: Download and burn the image file to SD card (https://drive.google.com/file/d/1ej6aDmI9ExDejRdJkBol5ps9nm_U_NV6/view?usp=drive_link), then boot the AXU3EG board.
Step 2: Extract and install DNNDK with "install.sh" in the vitis-ai_v1.2_dnndk Archive (on board).
Step 3: Copy and paste all files in tf_yolov3_motion_deploy to the working folder (on board).
Step 4: Run 'python3 tf_yolov3_voc_pic_V1.py'. The demo should now be running.

--------------------------------------------------------------------
