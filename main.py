'''
gifmaker

main.py
Dane Pilcher
'''

#!/usr/bin/python

import sys, getopt, argparse

from moviepy.editor import *

def main(argv):
    '''main function'''
    input_file_path = ''
    output_file_path = ''
    start_time_sec = 0
    start_time_min = 0
    end_time_sec = 0
    end_time_min = 0

    parser = argparse.ArgumentParser(description='Create a GIF.')
    # positional args
    parser.add_argument('filename', metavar='filename', type=str,
                        help='filepath to input video')
    parser.add_argument('start_time', metavar='start-time', type=str,
                        help='start time of GIF')
    parser.add_argument('end_time', metavar='end-time', type=str,
                        help='end time of GIF')
    
    # optional args 
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='turn on verbose output')
    
    # get args
    args = parser.parse_args()

    input_file_path = args.filename
    start_time_sec = int(args.start_time)
    end_time_sec = int(args.end_time)
    
    clip = (VideoFileClip(input_file_path)
            .subclip((start_time_min,start_time_sec),
                     (end_time_min,end_time_sec)))
    clip.write_gif("newgif.gif")
    
def raw_time_to_sec(raw_time):
    '''takes in a string raw_time in the format 00:00 and returns an
    integer value in seconds'''
    time = int(raw_time[:2]) * 60
    time += int(raw_time[2:])
    return time

if __name__ == "__main__":
    main(sys.argv[1:])
