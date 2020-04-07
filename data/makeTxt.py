import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'yolov3/data/Annotations'
txtsavepath = 'yolov3/data/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('yolov3/data/ImageSets/trainval.txt', 'w')
ftest = open('yolov3/data/ImageSets/test.txt', 'w')
ftrain = open('yolov3/data/ImageSets/train.txt', 'w')
fval = open('yolov3/data/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
