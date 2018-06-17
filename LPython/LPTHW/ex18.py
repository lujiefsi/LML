#function
def print_two(*args):
        args1, args2 = args
        print ("args1 == %r args2 == %r" %(args1, args2))
def print_one(args):
    print(args)
print_two("zed", "Shaw")
print_one(12)
print_one("1234")
