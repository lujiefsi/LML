'''
Created on Jun 27, 2018

@author: lujie
'''

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["a","b","c"])
happy_bday.sing_me_a_song()
