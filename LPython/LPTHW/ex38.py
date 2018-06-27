'''
Created on Jun 27, 2018

@author: lujie
'''

ten_things = "Apples orianges Crows telephone light sugar"

print("wait there's not 10 things in that list, let's fix that")

stuff = ten_things.split(' ')

more_stuff = ["day", "night","song","frisbee", "corn", "Banana", "Girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There's %d item now" % len(stuff))
print(stuff)
print(stuff[1])
print(stuff[-1])
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
