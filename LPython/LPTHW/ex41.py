'''
Created on Jun 28, 2018

@author: lujie
'''
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    print(WORDS)




