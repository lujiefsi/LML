#function
def print_two(*args):
        args1, args2 = args
        print ("args1 == %r args2 == %r" %(args1, args2))
def print_one(args):
    args1 = args
print_two("zed", "Shaw")
