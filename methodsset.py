# THIS SET WILL CREATE AN EMPTY DICTIONARY NOT AN EMPTY SET
a = {}
print(type(a))
  
#   an empty set can be created using the below syntax
b = set()
print(type(b))
# addong values to an empty set
b.add(4)
b.add(5)
# cannot add list to sets
# b.add([4,5,6]) 
# cannot add dictionary to sets
# b.add({4:5}) 
# can add tuple to sets
b.add((4,5,6))  
print(b)

# prints the length of the sets
print(len(b))   #3

# remove 5 from the set
b.remove(5)
print(b)
# b.remove(15) eill give error as 15 is not present in the set

print(b.pop())
print(b)
