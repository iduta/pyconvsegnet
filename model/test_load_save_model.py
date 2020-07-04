import torch
from models import  resnet, resstage, iresnet, resgroup, resgroupfix, iresgroup, iresgroupfix
from collections import OrderedDict

#m = iresnet.iresnet50()
#print(m)

#path = '/Users/ionut/Desktop/work/models_image_recognition/models_server/iresnet/iresnet50_epochs90_batch_size256/model_best.pth.tar'
#best_checkpoint = torch.load(path, map_location=torch.device('cpu'))
#print(best_checkpoint)
#m.load_state_dict(best_checkpoint['state_dict'], strict=True)

model_name = 'iresgroupfix'
depth = 152
m = iresgroupfix.iresgroupfix152()
load_path = '/Users/ionut/Desktop/work/models_image_recognition/models_server/iresnext_fix_card/iresnext_fix_card152_epochs90_batch_size256/'\
            + 'model_best.pth.tar'
save_path = '/Users/ionut/Desktop/work/models_image_recognition/models_server/models_iresnet/' + \
            model_name + '/' + model_name + str(depth) + '.pth'


state_dict = torch.load(load_path, map_location=torch.device('cpu'))['state_dict']

new_state_dict = OrderedDict()
for k, v in state_dict.items():
    name = k.replace("module.", "") # when the backbone model used DataParallel in training then we need to remove "module."
    new_state_dict[name] = v

torch.save(new_state_dict, save_path)

#print("Model state dict before:\n", m.state_dict())
print("Check load state dict: ", save_path)
m.load_state_dict(torch.load(save_path), strict=True)
#print("Model state dict after:\n", m.state_dict())
print("OK")

