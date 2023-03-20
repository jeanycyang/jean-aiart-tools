from PIL import Image
import os
import sys
import math

def round_to_64(n):
    return round(n / 64) * 64

def resize_image(filename, resolution=512): # 768 for SD 2.x
    img = Image.open(filename)

    width, height = img.size
    new_width, new_height = width, height

    if width > height:
        new_height = resolution
        new_width = round_to_64(int(float(width) / float(height) * new_height))
    else:
        new_width = resolution
        new_height = round_to_64(int(float(height) / float(width) * new_width))
    
    resized_img = img.resize((new_width, new_height))
    resized_img.save(filename)

    return new_width, new_height

def get_image_filenames(dir_path):
    extensions = [".jpg", ".jpeg", ".png"]
    images = []
    for filename in os.listdir(dir_path):
        if any(filename.endswith(ext) for ext in extensions):
            images.append(filename)
    return images

if __name__ == "__main__":
    dir_path = sys.argv[1]
    resolution = int(sys.argv[2])

    images = get_image_filenames(dir_path)
    for i in images:
        file_path = os.path.join(dir_path, i)
        w, h = resize_image(file_path, resolution)
        print("Resized {filename} to {w} x {h}".format(filename=i, w=w, h=h))