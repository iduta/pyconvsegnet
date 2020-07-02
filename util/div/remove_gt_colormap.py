import glob
import os.path
import numpy as np

from PIL import Image

array_3ch = np.array(Image.open("/home/ionut/Downloads/ade20k_dataset/ADE20K_2016_07_26/images/training/a/abbey/ADE_train_00000970_seg.png"))
array_1ch = array_3ch.astype(dtype=np.uint8)
pil_image = Image.fromarray(array_3ch.astype(dtype=np.uint8)).convert('L')
#pil_image.show()
#Image.fromarray(im_3ch.astype(dt))

#print(np.max(array_1ch))
print(array_3ch.shape)
print(array_3ch[10,10,:])
print("OK")

im = np.array(Image.open("/media/ionut/LaCie/ionut/datasets/ade20k/ADEChallengeData2016/annotations/training/ADE_train_00000003.png"))
print(im)
print(np.min(im), np.max(im))