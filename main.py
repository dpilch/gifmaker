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
    start_point_raw = raw_input("Start point:")
    end_point_raw = raw_input("End point:")
    start_point = raw_time_to_sec(start_point_raw)
    end_point = raw_time_to_sec(end_point_raw)
    
def raw_time_to_sec(raw_time):
    '''takes in a string raw_time in the format 00:00 and returns an
    integer value in seconds'''
    time = int(raw_time[:2]) * 60
    time += int(raw_time[2:])
    return time

main()
