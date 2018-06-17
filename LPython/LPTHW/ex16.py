# write file
from sys import argv

script, filename = argv

print ("We are going to erase %r" % filename)

target = open(filename, "w")
target.truncate()

target.write("test")
target.close()
