import pandas
import cv2
from glob import iglob
import os

'''
This script will convert multi-class coco-yolo dataset to single class yolo dataset
'''

#source_txt = 'data-cleaning/dataset/coco-raw/labels/val/'
#source_img = 'data-cleaning/dataset/coco-raw/images/val/'
# make sure destination is empty
#destination = '/data-cleaning/dataset/crowdhuman-coco-yolo/labels-half-v2/val/'

source_txt = 'data-cleaning/dataset/coco-raw/labels/train/'
source_img = 'data-cleaning/dataset/coco-raw/images/train/'
# make sure destination is empty
destination = 'data-cleaning/dataset/crowdhuman-coco-yolo/labels-half-v2/train/'

count = 0
for filename in sorted(iglob(source_txt + '*.txt')):
    count += 1
    print(count)
    file = open(filename, "r")
    filename_base = os.path.splitext(os.path.basename(filename))[0]
    #img = cv2.imread(source_img + filename_base + '.jpg')
    #H = img.shape[0]
    #W = img.shape[1]

    # make sure a empty file is written even if label is empty
    # open(destination + filename_base + '.txt', 'a')

    for row in file:
        row = row[:-1].split()
        #print(row)
        # filt small bbox

        if int(row[0]) == 0 and float(row[4])/float(row[3]) > 1.5 and row[1]< 0.2:
            # uncommand to reduce h of the box to a ratio
            #w = float(row[3])
            #h = float(row[4])/2
            #x = float(row[1])
            #y = (float(row[2])-float(row[4])/2) + h/2

            w = float(row[3])
            h = float(row[4])
            x = float(row[1])
            y = float(row[2])
            content = '0 ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n'
            #print(content)

            with open(destination + filename_base + '.txt', 'a') as file:
                file.write(content)

