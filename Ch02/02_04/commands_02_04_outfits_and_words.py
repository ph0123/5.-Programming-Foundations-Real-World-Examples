""" You Can Change an Outfit, But You Can't Change Your Words """

# create a closet full of clothes
closet = ['shirt','hat','pants','jacket','socks']
print(closet)
print(id(closet))

# remove a hat
closet.remove('hat')
print(closet)
print(id(closet))

# create a poor choice of words
words = "You're wearing that"
print(words)
print(id(words))


#both samples below will show different address of all strings.
# add more to the phrase before an object
words1 = words + ' because you look great!'
print(words1)
print(id(words1))


# add more to the phrase after an object
words1 = ' because you look great!' + words
print(words1)
print(id(words1))