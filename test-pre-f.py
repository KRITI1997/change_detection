import numpy as np
import os
import torch
import torch.nn as nn
import torch.utils.data as Data
from torch.autograd import Variable
from torch.nn import functional as F
import utils.transforms as trans
import utils.utils as util
import utils.metric as mc
import time
import datetime
import cv2
#import dataset.rs as dates

os.environ["CUDA_VISIBLE_DEVICES"] = "0"


#val_transform_det = trans.Compose([trans.Scale(256,256),])

#val_data = dates.Dataset('/dataset', '/dataset',
 #                            '/dataset/test.txt', 'val', transform=True,
  #                           transform_med=val_transform_det)
#val_loader = Data.DataLoader(val_data, batch_size=1,
  #                               shuffle=False, num_workers=4, pin_memory=True)
import model.siameseNet.dares as models
model = models.SiameseNet(norm_flag='l2')
#checkpoint = torch.load('/Users/sksingh/Desktop/DASNet-master/CDD_model_best.pth',
                            #map_location='cpu')

state_dict = torch.load('/Users/sksingh/Desktop/DASNet-master/CDD_model_best.pth', map_location=torch.device('cpu'))['state_dict']
net = model.load_state_dict(state_dict, strict = False)

print(net.summary())

#model.load_state_dict(checkpoint['state_dict'],strict='False')

print('load success')
#model = model.cuda()
save_change_map_dir ='the path to changemap'
save_roc_dir = 'the path to roc'
time_start = time.time()
#current_metric = validate(model, val_loader, save_change_map_dir, save_roc_dir)

elapsed = round(time.time() - time_start)
elapsed = str(datetime.timedelta(seconds=elapsed))
print('Elapsed {}'.format(elapsed))