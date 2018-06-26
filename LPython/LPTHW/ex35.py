'''
Created on Jun 26, 2018

@author: lujie
'''
from sys import exit

def bear_room():
    print()
def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")
    next = input()
    if "flee" in next:
        start()
def dead(message):
    print(message)
    exit(0)
def start():
    next = input(">");
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")
    
start()
    