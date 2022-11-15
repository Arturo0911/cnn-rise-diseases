# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WV6x5N_FDYwpjpdbbwBp6FePtuSr1tGL
"""

import tensorflow as tf
from tensorflow.keras import (
    regularizers,
    models,
    optimizers,
)
from PIL import Image
import os
from pprint import pprint
from google.colab import drive
from tensorflow.keras.layers import (
     Dense,
    Conv2D,
    MaxPooling2D,
    Activation,
    BatchNormalization,
    Dropout,
    Flatten
)
import os
import sys
from tensorflow.keras.callbacks import (ModelCheckpoint)
from tensorflow.keras.preprocessing.image import (
    array_to_img,
    img_to_array,
    load_img,
    ImageDataGenerator
)
import numpy as np



FILE_PATH = "/gdrive/My Drive/NewRiceImages"
drive.mount("/gdrive")
TRAIN_PATH = f"{FILE_PATH}/train"
TEST_PATH = f"{FILE_PATH}/test"
VALID_PATH = f"{FILE_PATH}/validator"

print(os.listdir(FILE_PATH))
print(len(os.listdir(TRAIN_PATH)))
print(len(os.listdir(TEST_PATH)))
print(len(os.listdir(VALID_PATH)))

from tensorflow.keras.datasets import fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images.shape

train_labels.shape
