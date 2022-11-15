#!/usr/bin/env python

from pprint import pprint
from PIL import Image
import os


def resizing_images():
    list_images = os.listdir("RiceImages")
    new_path = "NewRiceImages"
    for position, file in enumerate(list_images):
        img = Image.open(os.path.join("RiceImages", file))
        new_img = img.resize((64,64))

        new_img.save(f"{new_path}/rice_leave.{position}.png")


def set_location_images():
    new_name = "rice_leaf_healthy"
    list_images = os.listdir("NewRiceImages/rice_leaf_healthy/")

    for position, file in enumerate(list_images):
        img = Image.open(os.path.join("NewRiceImages/rice_leaf_healthy/", file))
        img.save(f"NewRiceImages/train/rice_leaf_healthy.{position}.png")

def main():

    #list_images = os.listdir("NewRiceImages")
    #for x in list_images:
    #    img = Image.open(os.path.join("NewRiceImages", x))
    #    print(img.shape)
    set_location_images()


if __name__ == "__main__":
    main()
