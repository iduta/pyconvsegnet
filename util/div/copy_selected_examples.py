
import os, glob, sys
import shutil


path_selected_examples = "/home/ionut/Desktop/work/cvpr2020/supplementary_material/supplementary_material_ade20k_examples"

path_source = "/home/ionut/Desktop/work/cvpr2020/backup/image_segmentation/val_MS_pyconv152_pyconvseg_stride8_noMergeStages/result/epoch_100/val_ms/ss/color/"
path_dest = "/home/ionut/Desktop/work/cvpr2020/supplementary_material/val_MS_pyconv152_pyconvseg_stride8_noMergeStages/"

files = glob.glob(os.path.join(path_selected_examples, "ADE_val*.jpg"))
print(files)

#dir_name = os.path.join("/", *dst.split('/')[:-1])

if not os.path.exists(path_dest):
    os.makedirs(path_dest)

for i in files:
    im_name = i.split('/')[-1][:-3] + 'png'
    shutil.copy2(path_source+im_name, path_dest)
