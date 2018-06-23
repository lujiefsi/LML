'''
Created on Jun 23, 2018

@author: lujie
'''
poem='''
\t student should
good good study, day day up
'''

print(poem)

def returnThree(begin):
    return begin,begin+1,begin+2
first,second,third = returnThree(10)

print ("first = %d, second= %d, third = %d" % returnThree(1))

print("first=",first,"second=", second,"third=",third)