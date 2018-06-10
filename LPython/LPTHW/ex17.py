# copy file
from sys import argv

script, from_file, to_file = argv

print "copy from", from_file, "to", to_file

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)

out_file = open(to_file, "w")
out_file.write(in_data)
print "Done!"
out_file.close()
in_file.close()
