'''
gifmaker

main.py
Dane Pilcher
'''

from moviepy.editor import *

def main():
    '''main function'''
    print "gifmaker"
    file_path = raw_input("Filepath:")
    '''
    start_point_raw = raw_input("Start point:")
    end_point_raw = raw_input("End point:")
    start_point = raw_time_to_sec(start_point_raw)
    end_point = raw_time_to_sec(end_point_raw)
    '''
    start_point_min = int(raw_input("Start point minute:"))
    start_point_second = int(raw_input("Start point second:"))
    end_point_min = int(raw_input("End point minute:"))
    end_point_second = int(raw_input("End point second:"))
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
