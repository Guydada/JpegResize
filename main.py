import os
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt


def resize_folder(output_width=640, output_height=480):
    input_path = input("Enter folder path for resizing: ")
    output_path = input_path + '\\Resized'
    try:
        os.mkdir(output_path)
    except FileExistsError:
        print("Folder already exists, continuing ")
    folder = os.listdir(input_path)
    folder.pop(folder.index("Resized"))
    for filename in folder:
        image = "\\".join([input_path, filename])
        output_image = "\\".join([output_path, filename])
        try:
            dim_resized = resize_image_crop(image, output_image, output_width, output_height)
            print("Done for: {}, output shape: {}".format(filename, dim_resized))
        except FileExistsError:
            print("Failed for: {} because file already exists. Delete older exports and try again".format(filename))


def resize_image(input_path, output_path, output_width, output_height):
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    output_dim = (output_width, output_height)
    resized = cv2.resize(image, output_dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(output_path, resized)


def resize_image_crop(input_path, output_path, output_width, output_height):
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    (h, w) = image.shape[:2]
    r = output_height / float(h)
    dim = (int(w * r), output_height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resized = resized[:,107:747]
    cv2.imwrite(output_path, resized)
    dim_resized = resized.shape[:2]
    return dim_resized


resize_folder()
