#!/usr/bin/env python

import tensorflow as tf
from tensorflow.keras import models
from tensorflow.python.keras.models import (
    load_model,
    model_from_json
)
from tensorflow.python.keras.initializers import glorot_uniform
from tensorflow.keras.utils import CustomObjectScope
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import (
    load_img,
    img_to_array,
    array_to_img
)
from tensorflow.keras.applications import imagenet_utils
from PIL import Image



def prediction():
    K.reset_uids()
    model = "models/riceai_json_model_2.json"
    weights = "models/final_model_2.hdf5"

    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        with open(model, 'r') as f:
            model = model_from_json(f.read())
            model.load_weights(weights)
        

    img = Image.open("LastRiceImages/test/rice_leaf_healthy/rice_leaf_healthy.18.png")
    # img = Image.open("images.jpg")
    img = img_to_array(load_img('LastRiceImages/test/rice_leaf_healthy/rice_leaf_healthy.18.png', target_size=(224,224)))/255.0
    img = img.reshape(1, 224, 224, 3)

    result = model.predict(img)
    pre = imagenet_utils.decode_predictions(result)
    print(result[0][0])
    print(pre)

def main():
    try:
        prediction()
    except Exception as e:
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        exit(0)



if __name__ == "__main__":
    main()