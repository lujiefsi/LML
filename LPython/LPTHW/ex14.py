# prompting
from sys import argv

script, user_name = argv
prompt = ">"

print ("Hi %s, I am the %s scirpt" % (user_name, script))
print ("Do you like me %s" %user_name)
likes = input(prompt)
print (likes)
