#!/usr/bin/env python

from pprint import pprint
from PIL import Image
import os

"""
this is a simple snippet code
"""

def resizing_images() -> None:
    list_images = os.listdir("RiceImages")
    new_path = "NewRiceImages"
    for position, file in enumerate(list_images):
        img = Image.open(os.path.join("RiceImages", file))
        new_img = img.resize((64,64))

        new_img.save(f"{new_path}/rice_leave.{position}.png")


def set_location_images(name_dir: str, iteration_num: int) -> None:
    new_name = f"rice_leaf_{name_dir}"
    list_images = os.listdir(f"NewRiceImages/rice_leaf_{name_dir}/")

    for position, file in enumerate(list_images):
        img = Image.open(os.path.join(f"NewRiceImages/rice_leaf_{name_dir}/", file))
        img.save(f"NewRiceImages/train/rice_leaf_{name_dir}.{position}.png")

def main():

    #list_images = os.listdir("NewRiceImages")
    #for x in list_images:
    #    img = Image.open(os.path.join("NewRiceImages", x))
    #    print(img.shape)
    # set_location_images()

    try:
        list_images = os.listdir("yellow")
        for pos, file in enumerate(list_images):
            img = Image.open(os.path.join("yellow", file))
            new_img = img.resize((64,64))
            new_img.save(f"new_yellow/rive_leaf_yellow.{pos+12}.png")
    except Exception as e:
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
