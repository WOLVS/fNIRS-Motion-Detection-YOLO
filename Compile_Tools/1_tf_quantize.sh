#!/bin/sh

# rm -rf vai_*

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

TF_NETWORK_PATH=modle/${OBJECT_TYPE}/pb_file/keras-yolo3-${OBJECT_TYPE}.pb
INPUT_SHAPES=?,256,512,3
INPUT_NODES=input_1
OUTPUT_NODES=conv2d_59/convolution,conv2d_67/convolution,conv2d_75/convolution

# Output path
OUTPUT_DIR=modle/${OBJECT_TYPE}/vai_q_output

# total batch number in count
#CALIB_ITER=184
CALIB_ITER=19

#--------------------- USER MODIFY AREA-----------------------------#




vai_q_tensorflow quantize --input_frozen_graph ${TF_NETWORK_PATH} \
			  --input_shapes ${INPUT_SHAPES} \
			  --input_fn input_fn.calib_input \
			  --output_dir ${OUTPUT_DIR} \
			  --input_nodes ${INPUT_NODES} \
			  --output_nodes ${OUTPUT_NODES} \
			  --calib_iter ${CALIB_ITER} \



