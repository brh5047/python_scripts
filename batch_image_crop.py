import cv2
import os
path = ''
save = ''

#create file path list
image_files = [f for f in os.listdir(path) if f.endswith('.png')]  

for file in image_files:

    y = 190 #Y origin (starts in upper lefthand corner)
    x = 600 #X origin (starts in upper lefthand corner)
    w = 1020
    h = 700

    writer = file.split('.')[0]

    sample_img = cv2.imread(path + str(file))
    crop_img = sample_img[y:y+h,x:x+w]
    cv2.imwrite(save + '/' + writer  + '_crop.png', crop_img)
