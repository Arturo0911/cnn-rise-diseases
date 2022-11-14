#!/usr/bin/env python


## author: Arturo Negreiros for my tesis
## Date from 13-11-2022 to: ???


"""
Taking care about others resesarchings


In China, using the same concept, for rice disease
They got the following information:

    Their CNN model arcnitecture consists of 4 convolution layers,
    3 max pooling layers, fully connected layers and softmax layers.
    This means that in the model the convolution process is carried out
    4 times and the re-shaping process is 3 times before entering the 
    fully connected aritificial neural network. The process of finding
    the model uses  maximun iteration parameter of 200. In the CNN model, each
    convolution layaer contains 16 filters with a size of 3x3 and the max
    pooling layres has a pool size of 2x2 and a stride of 2.
"""


import tensorflow as tf
from tensorflow.keras.layers import (
    Dense,
    Conv2D,

)
