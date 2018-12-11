the_count = [1,2,3,4,6]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarter']

for number in the_count:
    print ("This count", number)
for fruit in fruits:
    print("a fruits of type", fruit)
for i in change:
    print("i got change %r" %i)

elements = []

for i in range(0,6):
    print("Adding %d to the list." %i)
    elements.append(i)

for i in elements:
    print("element was %d" %i)
