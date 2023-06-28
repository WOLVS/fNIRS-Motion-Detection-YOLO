#!/bin/bash


#--------------------- USER MODIFY AREA-----------------------------#

# ATTENTION: Please confirm PATH after launch Xilinx Runtime Docker ! 
# concrete
# helmet
# pcb
# pedestrian
# thermal
# vehicle
# fire
# office
#-------- model object type ----------

OBJECT_TYPE=motion

#-------------------------------------

TARGET=AXU3EG_DPU_B1600

NET_NAME=tf_yolov3_${OBJECT_TYPE}
KERNEL_PATH=modle/${OBJECT_TYPE}/vai_c_output_${TARGET}

#--------------------- USER MODIFY AREA-----------------------------#






CUR_DIR=$(pwd)
echo "------------------------------------------------------"
echo "------------------- Start Compiling ------------------"
echo "------------------------------------------------------"
echo $'\n'
echo " Entering elf file path..."
echo $'\n'
cd ${KERNEL_PATH}

aarch64-xilinx-linux-gcc --sysroot=/opt/vitis_ai/petalinux_sdk/sysroots/aarch64-xilinx-linux \
		      -fPIC -shared dpu_${NET_NAME}.elf -o libdpumodel${NET_NAME}.so

cd ${CUR_DIR}


echo " Kernal file: libdpumodel${NET_NAME}.so will be generated. "
echo $'\n'
echo " Default Output Path: ${KERNEL_PATH} "
echo $'\n'
echo "------------------------------------------------------"
echo "-------------------- Task Done -----------------------"
echo "------------------------------------------------------"

echo " copy to deploy project path ../code/deploy_in_board/Alinx_DNN/${TARGET}/${NET_NAME}_deploy/"
#cp ${KERNEL_PATH}/*.so ../code/deploy_in_board/Alinx_DNN/${NET_NAME}_deploy/
