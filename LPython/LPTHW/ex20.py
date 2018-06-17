'''
Created on Jun 17, 2018

@author: lujie

function and file
'''

from sys import argv
script, input_file = argv
def print_all(f):
    print(f.read())
def remind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())
current_file = open(input_file)
print("print all content")
print_all(current_file)
print("******************")

remind(current_file)
current_line=1
print_a_line(current_line, current_file)
current_line+=1
print_a_line(current_line, current_file)
current_line+=1
print_a_line(current_line, current_file)

    
