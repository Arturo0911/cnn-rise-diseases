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

    

    try:
        print("intiializing with the path of the train")

        list_images_train_healthy = os.listdir("NewRiceImages/train/rice_leaf_healthy")
        list_images_train_yellow = os.listdir("NewRiceImages/train/rice_leaf_yellow")


        list_images_test_healthy = os.listdir("NewRiceImages/test/rice_leaf_healthy")
        list_images_test_yellow = os.listdir("NewRiceImages/test/rice_leaf_yellow")



        # healthy
        for pos, file in enumerate(list_images_train_healthy):
            img = Image.open(os.path.join("NewRiceImages/train/rice_leaf_healthy", file))
            new_img = img.resize((224,224))
            new_img.save(f"LastRiceImages/train/rice_leaf_healthy/rice_leaf_healthy.{pos}.png")
        

        # yellow
        for pos, file in enumerate(list_images_train_yellow):
            img = Image.open(os.path.join("NewRiceImages/train/rice_leaf_yellow", file))
            new_img = img.resize((224,224))
            new_img.save(f"LastRiceImages/train/rice_leaf_yellow/rice_leaf_yellow.{pos}.png")
        

        # test healthy
        for pos, file in enumerate(list_images_test_healthy):
            img = Image.open(os.path.join("NewRiceImages/test/rice_leaf_healthy", file))
            new_img = img.resize((224,224))
            new_img.save(f"LastRiceImages/test/rice_leaf_healthy/rice_leaf_healthy.{pos}.png")

        
        # test yellow
        for pos, file in enumerate(list_images_test_yellow):
            img = Image.open(os.path.join("NewRiceImages/test/rice_leaf_yellow", file))
            new_img = img.resize((224,224))
            new_img.save(f"LastRiceImages/test/rice_leaf_yellow/rice_leaf_yellow.{pos}.png")
        



        print("intiializing with the path of the test")
    except Exception as e:
        print(str(e))
        exit(1)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)


if __name__ == "__main__":
    main()
