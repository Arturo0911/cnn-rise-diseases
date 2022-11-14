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

        new_img.save(f"{new_path}/rice_leave_{position}.png")


def set_location_images():
    pass


def main():

    list_images = os.listdir("NewRiceImages")
    for x in list_images:
        img = Image.open(os.path.join("NewRiceImages", x))
        print(img.shape)
    


if __name__ == "__main__":
    main()
