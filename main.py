'''
gifmaker

main.py
Dane Pilcher
'''

#!/usr/bin/python

import sys, getopt

from moviepy.editor import *

def main(argv):
    '''main function'''
    
    file_path = sys.argv[0]
    raw_start_time = int(sys.argv[1])
    raw_end_time = int(sys.argv[2])
    start_point_min = 0
    start_point_second = raw_start_time
    end_point_min = 0
    end_point_second = raw_end_time
    clip = (VideoFileClip(file_path)
            .subclip((start_point_min,start_point_second),(end_point_min,end_point_second)))
    clip.write_gif("newgif.gif")

def raw_time_to_sec(raw_time):
    '''takes in a string raw_time in the format 00:00 and returns an
    integer value in seconds'''
    time = int(raw_time[:2]) * 60
    time += int(raw_time[2:])
    return time

if __name__ == "__main__":
    main(sys.argv[1:])
