""" What Makes Up an Object? """

# examine a string object
print('shirt')
print(type('shirt'))
print(dir('shirt')) #show all function with string type.

# use upper method on a string object
print('shirt'.upper())

# examine IDs of different string objects
print(id('shirt'))
print(id('pants'))

# examine an integer object
print(id(1))
print(dir(1))

# examine ID and attributes of functions
print(id(id))  #show the object's memory address and
#will be different for each time you run the program.
print(dir(dir))
