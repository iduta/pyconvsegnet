import glob
import os.path
import numpy as np
#import cv

from PIL import Image
import os, glob, sys

#path_annotations = "/home/ionut/Downloads/ade20k_dataset/ADEChallengeData2016/original_annotations"
path_annotations = "/home/ionut/Desktop/work/cvpr2020/benchmark/cityscapes/pyconv152_pyconvseg_stride8_noMergeStages_weght_fine_coarse__fine_train_val_200epochs_crop1025/result/epoch_200/val_ms/ss/gray"

files = glob.glob(os.path.join(path_annotations, "*leftImg8bit.png") )

# quit if we did not find anything
if not files:
    print("Did not find any files. Please consult the README.")

#trainID = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#originalID = [7, 8, 11, 12, 13, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33]

#(trainID, originalID)
trainID_to_originalID = [(0, 7), (1, 8), (2, 11), (3, 12), (4, 13), (5, 17), (6, 19), (7, 20), (8, 21), (9, 22),
                         (10, 23), (11, 24), (12, 25), (13, 26), (14, 27), (15, 28), (16, 31), (17, 32), (18, 33)]
# a bit verbose
print("Processing {} annotation files".format(len(files)))

progress = 0
print("Progress: {:>3} %".format(progress * 100 / len(files)), end=' ')
for f in files:
    # create the output filename
    dst = f.replace("gray", "challenge_format")
    dir_name = os.path.join("/", *dst.split('/')[:-1])
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    im = np.array(Image.open(f))
    new_im = np.zeros(im.shape, dtype=np.uint8)

    for i in trainID_to_originalID:
        new_im[im == i[0]] = i[1]

    if np.sum(new_im == 0) > 0:
        print("Warning, some pixels are still zero ... ")

    pil_image = Image.fromarray(new_im.astype(dtype=np.uint8))
    pil_image.save(dst)

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