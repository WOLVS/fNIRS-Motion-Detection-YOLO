import cv2
from sklearn import preprocessing

import tensorflow as tf
import os
import cv2
from tensorflow.python.platform import gfile
import numpy as np
from tqdm import tqdm
import argparse

_R_MEAN = 123.68
_G_MEAN = 116.78
_B_MEAN = 103.94

MEANS = [_B_MEAN,_G_MEAN,_R_MEAN]




#============================================================================================
#==================================== yolov3 Calibration ====================================
#============================================================================================


def letterbox_image(image, size):
    '''resize image with unchanged aspect ratio using padding'''
    ih, iw, _ = image.shape
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)

    image = cv2.resize(image, (nw,nh), interpolation=cv2.INTER_LINEAR)
    new_image = np.ones((h,w,3), np.uint8) * 128
    h_start = (h-nh)//2
    w_start = (w-nw)//2
    new_image[h_start:h_start+nh, w_start:w_start+nw, :] = image
    return new_image


def pre_process(image, model_image_size):
    image = image[...,::-1]
    image_h, image_w, _ = image.shape

    # image preprocessing
    if model_image_size != (None, None):
        assert model_image_size[0]%32 == 0, 'Multiples of 32 required'
        assert model_image_size[1]%32 == 0, 'Multiples of 32 required'
        boxed_image = letterbox_image(image, tuple(reversed(model_image_size)))
    else:
        new_image_size = (image_w - (image_w % 32), image_h - (image_h % 32))
        boxed_image = letterbox_image(image, new_image_size)
    image_data = np.array(boxed_image, dtype='float32')
    image_data /= 255.
    image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

    return image_data

#============================================================================================
#==================================== yolov3 Calibration ====================================
#============================================================================================





def mean_image_subtraction(image, means):
  B, G, R = cv2.split(image)
  B = B - means[0]
  G = G - means[1]
  R = R - means[2]
  image = cv2.merge([R, G, B])
  return image


def central_crop(image, crop_height, crop_width):
  image_height = image.shape[0]
  image_width = image.shape[1]
  offset_height = (image_height - crop_height) // 2
  offset_width = (image_width - crop_width) // 2
  return image[offset_height:offset_height + crop_height, offset_width:
               offset_width + crop_width, :]


eval_batch_size = 1
def eval_input(iter, eval_image_dir, eval_image_list, class_num):
    images = []
    labels = []
    line = open(eval_image_list).readlines()
    for index in range(0, eval_batch_size):
        curline = line[iter * eval_batch_size + index]
        [image_name, label_id] = curline.split(' ')
        image = cv2.imread(eval_image_dir + image_name)
        image = central_crop(image, 224, 224)
        image = mean_image_subtraction(image, MEANS)
        images.append(image)
        labels.append(int(label_id))
    lb = preprocessing.LabelBinarizer()
    lb.fit(range(0, class_num))
    labels = lb.transform(labels)
    return {"input": images, "labels": labels}



'''
def calib_input(iter):
-----A function that provides input data for the calibration-----
Args:
iter: A `int` object, indicating the calibration step number
Returns:
dict( placeholder_name, numpy.array): a `dict` object, which will be
fed into the model
-----------------------------------------------------------------
image = load_image(iter)
preprocessed_image = do_preprocess(image)
return {"placeholder_name": preprocessed_images}
'''

#calib_image_dir = "../data/voc2007_test/images/"
#calib_image_list = "../data/voc2007_test/test.txt"

calib_image_dir = "modle/motion/JPEGImages/"
calib_image_list = "modle/motion/motion_test.txt"

calib_batch_size = 20
def calib_input(iter):
    images = []
    line = open(calib_image_list).readlines()
    for index in range(0, calib_batch_size):
        curline = line[iter * calib_batch_size + index]
        calib_image_name = curline.strip()
        image = cv2.imread(calib_image_dir + calib_image_name )  
        image = pre_process(image, (416,416))
        images = np.array(image,dtype=np.float32)

    return {"input_1": images} #input nodes: input_1, you can check your pb file via netron


