'''
gifmaker

main.py
Dane Pilcher
'''

#!/usr/bin/python

import sys

from moviepy.editor import *

def main():
    '''main function'''
    clip = (VideoFileClip(file_path)
            .subclip((start_point_min,start_point_second),(end_point_min,end_point_second)))
    clip.write_gif("newgif1.gif")

def raw_time_to_sec(raw_time):
    '''takes in a string raw_time in the format 00:00 and returns an
    integer value in seconds'''
    time = int(raw_time[:2]) * 60
    time += int(raw_time[2:])
    return time

main()
