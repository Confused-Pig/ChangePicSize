#!/user/bin/python3
# Author:Confused Pig
# -*- coding: utf-8 -*-

# @Time    : 2020/12/29  21:01
# @Author  : Confused Pig
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import os
import cv2


def ResizePic(path,save_path,dim):
    i = 1
    file_name = os.listdir(path + '/')
    for img in file_name:
        image = cv2.imread(path + '/' + img)
        image_size = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(save_path + '/' + str(i) + '.jpg', image_size)
        i = i + 1

d = ResizePic('Image','Out_image',dim=(64,64))