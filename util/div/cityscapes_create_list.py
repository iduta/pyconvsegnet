import os
'''
#for cityscapes dataset fine

split = 'test' # train val test
path_images = '/home/ionut/Downloads/cityscapes_dataset/leftImg8bit_trainvaltest/leftImg8bit/' + split + '/'
path_save_list = '/home/ionut/Downloads/cityscapes_dataset/list/fine_' + split + '.txt'

relativ_base_images = '/leftImg8bit_trainvaltest/leftImg8bit/' + split + '/'
relativ_base_gt = '/gtFine_trainvaltest/gtFine/' + split + '/'
end_gt = 'gtFine_labelTrainIds.png'


images = []

for r, d, f in os.walk(path_images):
    for file in f:
        if '.png' in file:
            images.append(os.path.join(r, file))

#/home/ionut/Downloads/cityscapes_dataset/leftImg8bit_trainvaltest/leftImg8bit/train/bochum/bochum_000000_000313_leftImg8bit.png
#bochum_000000_000313_gtFine_labelTrainIds.png

relativ_path_images = []
relativ_path_gt = []
with open(path_save_list, 'w') as f:

    for im in images:
        sp = im.split("/")
        im_path = relativ_base_images + sp[-2] + '/' + sp[-1]
        gt_path = relativ_base_gt + sp[-2] + '/' + sp[-1][:-15] + end_gt
        relativ_path_images.append(im_path)
        relativ_path_gt.append(gt_path)
        if split == 'test':
            line = im_path + '\n'
        else:
            line = im_path + ' ' + gt_path + '\n'
        f.write(line)


'''




#for cityscapes dataset coarse


split = 'train_extra' # train val test
path_images = '/home/ionut/Downloads/cityscapes_dataset/leftImg8bit_trainextra/leftImg8bit/' + split + '/'
path_save_list = '/home/ionut/Downloads/cityscapes_dataset/list/coarse_' + 'train' + '.txt'

relativ_base_images = '/leftImg8bit_trainextra/leftImg8bit/' + split + '/'
relativ_base_gt = '/gtCoarse/gtCoarse/' + split + '/'
end_gt = 'gtCoarse_labelTrainIds.png'


images = []

for r, d, f in os.walk(path_images):
    for file in f:
        if '.png' in file:
            images.append(os.path.join(r, file))

#/home/ionut/Downloads/cityscapes_dataset/leftImg8bit_trainvaltest/leftImg8bit/train/bochum/bochum_000000_000313_leftImg8bit.png
#bochum_000000_000313_gtFine_labelTrainIds.png

relativ_path_images = []
relativ_path_gt = []
with open(path_save_list, 'w') as f:

    for im in images:
        sp = im.split("/")
        im_path = relativ_base_images + sp[-2] + '/' + sp[-1]
        gt_path = relativ_base_gt + sp[-2] + '/' + sp[-1][:-15] + end_gt
        relativ_path_images.append(im_path)
        relativ_path_gt.append(gt_path)
        if split == 'test':
            line = im_path + '\n'
        else:
            line = im_path + ' ' + gt_path + '\n'
        f.write(line)


