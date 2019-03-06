# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:42:58 2019

@author: maxua
"""

import  os

exe = 'ffmpeg -r 30 -i'
inputpath = 'F:/LimbLab1/20190304/'
inputfile = '20190304_Greyson_cage_15114300_01.h264'
outputpath = 'F:/LimbLab1/20190304/mp4/'
outputfile = '20190304_Greyson_cage_15114300_01.mp4'
mystr = ''.join((exe, ' ', inputpath, inputfile, ' ', outputpath, outputfile))

b = os.popen(mystr)
print(b)