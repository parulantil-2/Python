myDict = {
    "Fast": "In a Quick Manner",
    "Parul":"A Coder",
    "Marks":[1,2,5],
    "anotherDict":{'Parul':'Player'},
    1:2
}
#Dictionary methods
#Print the type of dictionary
print(type(myDict.keys()))
#Print the keys of the dictionary
print(list(myDict.keys()))
#Print the values of the dictionary
print(myDict.values())
#print the (key values) for all contents of the dictionary
print(myDict.items())
# update the dictionary
print(myDict)
updateDict ={
    "Lovish":"Friend",
    "Divya" : "Friend",
    "Payal": " Friend",
    "Parul": "A Dancer"
}
# update the dictionary by adding key-value pairs from updateDict
myDict.update(updateDict)
print(myDict)

# prints value associated with key harry
print(myDict.get("Parul2"))  
print(myDict["Parul2"]) 

# difference btwn .get and []syntax in dictionary
print(myDict.get("Parul2"))   # if Parul2 not present in dictionary it will return none
print(myDict["Parul2"])       # if  Parul2 not present in dictionary it will return error
