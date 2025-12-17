#!/usr/bin/env python3

from PIL import Image

ASCII_CHARS = "@#$%?*+;:,. "

def resize_image(image,new_width=100):
    width,height = image.size
    aspect_ratio =  height/width
    new_height = int(new_width * aspect_ratio * 0.5)
    return image.resize((new_width,new_height))


def grayscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = pixel * len(ASCII_CHARS)  // 256
        ascii_str += ASCII_CHARS[index]

    return  ascii_str

def image_to_ascii(path,width=100):
    image = Image.open(path)
    image = resize_image(image)
    image = grayscale(image)
    ascii_str = pixel_to_ascii(image)
    img_width = image.size[0]
    
    for i in  range(0,len(ascii_str),img_width):
         print(ascii_str[i:i+img_width])
img1 = "download.jfif"
image_to_ascii(img1,width=100)
