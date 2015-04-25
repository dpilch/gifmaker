'''
gifmaker

main.py
Dane Pilcher
'''

#!/usr/bin/python

import sys, argparse, os

from moviepy.editor import *

def main():
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
    parser.add_argument('-r', '--replay', action='store_true',
                        help='replay GIF (default)')
    parser.add_argument('-R', '--no-replay', action='store_true',
                        help='turn off GIF replay')
    parser.add_argument('-l', '--loop', action='store_true',
                        help='attempt to make a looping GIF')
    parser.add_argument('-o', '--output', metavar='filename', type=str,
                        help='filepath to output file')
    
    # get args
    args = parser.parse_args()
    
    # supress output if verbose is off
    sys.stdout = open(os.devnull, 'w')
    if args.verbose:
        sys.stdout = sys.__stdout__

    # if args.
    
    input_file_path = args.filename
    output_file_path = input_file_path[:-3] + 'gif'
    if args.output:
        output_file_path = args.output
    start_time_sec = raw_time_to_sec(args.start_time)
    start_time_min = raw_time_to_min(args.start_time)
    end_time_sec = raw_time_to_sec(args.end_time)
    end_time_min = raw_time_to_min(args.end_time)
    
    clip = (VideoFileClip(input_file_path)
            .subclip((start_time_min,start_time_sec),
                     (end_time_min,end_time_sec))).resize(0.3)
    try:
        clip.write_gif(output_file_path)
    except:
        print 'Error'
    
    sys.stdout = sys.__stdout__

def raw_time_to_min(raw_time):
    '''takes in a string raw_time in the format 00:00.00 and returns a int 
    alue in minutes'''
    time = float(raw_time[:2])
    return time

def raw_time_to_sec(raw_time):
    '''takes in a string raw_time in the format 00:00.00 and returns a
    float value in seconds'''
    time = float(raw_time[3:])
    return time

if __name__ == "__main__":
    main()
