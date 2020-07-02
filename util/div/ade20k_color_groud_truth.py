import glob
import os.path
import numpy as np
#import cv

from PIL import Image
import os, glob, sys

path_annotations = "/home/ionut/Downloads/ade20k_dataset/ADEChallengeData2016/original_annotations"

files = glob.glob(os.path.join(path_annotations, "*", "ADE*.png") )

# quit if we did not find anything
if not files:
    print("Did not find any files. Please consult the README.")

colors = np.loadtxt("ade20k_colors_original.txt").astype('uint8')
print(colors)

# a bit verbose
print("Processing {} annotation files".format(len(files)))

progress = 0
print("Progress: {:>3} %".format(progress * 100 / len(files)), end=' ')
for f in files:
    # create the output filename
    dst = f.replace("original_annotations", "original_color_annotations")
    dir_name = os.path.join("/", *dst.split('/')[:-1])
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    grey_im = np.array(Image.open(f))

    color_im = Image.fromarray(grey_im.astype(np.uint8)).convert('P')
    color_im.putpalette(colors)

    color_im.save(dst)

    # status
    progress += 1
    print("\rProgress: {:>3} %".format(progress * 100 / len(files)), end=' ')

'''
im = np.array(Image.open('/home/ionut/Downloads/ade20k_dataset/ADEChallengeData2016/original_annotations/training/ADE_train_00000001.png'))
print(np.min(im), np.max(im))

new_im = im - 1

pil_image = Image.fromarray(new_im.astype(dtype=np.uint8))
pil_image.show()
pil_image.save("/home/ionut/Desktop/tmp/ADE_train_00000001.png")


im2 = np.array(Image.open('/home/ionut/Desktop/tmp/ADE_train_00000001.png'))



print(im)
print(new_im)
print(im2)
'''