import os
#dir = '/home/zyx/data/pic/'+str(a)+'/'
#label = a
import glob
#dir_without_shift_train_A = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/without_shift/train/A/'
#dir_without_shift_train_B = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/without_shift/train/B/'
#dir_without_shift_train_OUT = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/without_shift/train/OUT/'

#dir_subset_train_A = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Real/subset/train/A/'
#dir_subset_train_B = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Real/subset/train/B/'
#dir_subset_train_OUT = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Real/subset/train/OUT/'

#dir_without_shift = 'D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/without_shift/'
dir_real = '/Users/sksingh/Downloads/val'

dir_val_A = '/Users/sksingh/Downloads/val/A/'
dir_val_B = '/Users/sksingh/Downloads/val/B/'
dir_val_OUT = '/Users/sksingh/Downloads/val/label/'





files_val_A = os.listdir(dir_val_A)
files_val_B = os.listdir(dir_val_B)
files_label= os.listdir(dir_val_OUT)

#paths = glob.glob(os.path.join(path, '*.jpg'))

#files_without_shift = os.listdir(dir_without_shift)
#files_real = os.listdir(dir_real)
#files.sort()

#files_with_shift_val_OUT = glob.glob(os.path.join(dir_with_shift_val_OUT,'*.bmp'))


#train = open('D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/train.txt','a')
val = open('/Users/sksingh/Desktop/DASNet-master/dataset/val1.txt', 'a')

#i = 1
#for file in files_with_shift:

#for file_with_shift_train_A,file_with_shift_train_B,file_with_shift_train_OUT in files_with_shift_train_A,files_with_shift_train_B,files_with_shift_train_OUT:
#    train.write('D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/with_shift/train/A/'+file_with_shift_train_A + '\n')
#    train.write('D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/with_shift/train/B/'+file_with_shift_train_B + '\n')
#    train.write('D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/with_shift/train/OUT/' + file_with_shift_train_OUT + '\n')



for i in range(64):
    val.write('val/A/' + files_val_A[i] + ' ')
    val.write('val/B/' + files_val_B[i] + ' ')
    #val.write('D:/xunleiDownload/DASNet-master/DASNET/dataset/ChangeDetectionDataset/Model/with_shift/val/OUT/' + files_with_shift_val_OUT[i] + '\n')
    #val.write(files_with_shift_val_OUT[i] + '\n')
    val.write('val/label/' + files_label[i] + '\n')
    #print(i * 2)
    #print(" ")



'''
for file in files:
    if i<29000:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name =  str(dir) +  file + ' ' + str(int(label)) +'\n'
        train.write(name)
        i = i+1
        print(i)
    else:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = str(dir) +file + ' ' + str(int(label)) +'\n'
        val.write(name)
        i = i+1
        print(i)

'''
val.close()
