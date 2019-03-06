# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:55:40 2019

@author: maxua
"""
#scp pi@10.106.56.16:./Videos/20190304_Greyson_cage_17042900_01.h264 F:/LimbLab1/20190304/
import fnmatch, os

exe = 'ffmpeg -r 30 -i'
source_path = 'H:/LimbLab5/Video20190304/'
target_path = 'H:/LimbLab5/Video20190304/mp4/'

h264_list = fnmatch.filter(os.listdir( ''.join((source_path, '/')) ), "*.h264")
for each in h264_list:
    sourcefile = ''.join((source_path, each))
    #print(sourcefile)
    temp = ''.join((each[:-5],'.mp4'))
    targetfile = ''.join((target_path, temp))
    #print(targetfile)
    my_str = ''.join((exe, ' ', sourcefile, ' ', targetfile))
    print(my_str)
    b = os.popen(my_str)
    print(b)



