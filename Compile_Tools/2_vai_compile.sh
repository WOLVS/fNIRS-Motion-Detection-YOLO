#!/bin/sh

#--------------------- USER MODIFY AREA-----------------------------#
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
TF_NETWORK_PATH=modle/${OBJECT_TYPE}

DEPLOY_MODEL_PATH=${TF_NETWORK_PATH}/vai_q_output
OUTPUT_PATH=${TF_NETWORK_PATH}/vai_c_output_${TARGET}

ARCH=hardware/${TARGET}/${TARGET}.json

#--------------------- USER MODIFY AREA-----------------------------#

vai_c_tensorflow --frozen_pb ${DEPLOY_MODEL_PATH}/deploy_model.pb \
                 --arch ${ARCH} \
		 		 --output_dir ${OUTPUT_PATH}/ \
				 --net_name ${NET_NAME} \
				 --quant_info

