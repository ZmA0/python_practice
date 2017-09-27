# -*- coding:utf-8 -*-
'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
import os
from PIL import Image
def modify(image):
    im=Image.open(image)
    width,height=im.size
    if height >1136 or width >640:
        th=height/1136
        td=width/640
        ts=max(th,td)
        nh=int(height/ts)
        nw=int(width/ts)
        im.resize((nw,nh))
        im.save(image)
        print ('have modified')
    else:
        print ('there is no need')

for i in os.listdir('./0005_pic/'):
    modify('./0005_pic/'+i)

