'''
Created on Jul 5, 2018

@author: lujie
'''
from sys import exit

from random import randint

class Scence(object):
    
    def enter(self):
        print("This scence is not yet configured. subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n -------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scence):
    quips = {"you died,, You kinda suck at this",
             "your mom would be proud... if she were samrter",
             "such a luser",
             "I have a samall puppy that's better at this "}
    def enter(self):
        print(Death.quips[randint(0,len(self.quips))])
        exit(1)
        
