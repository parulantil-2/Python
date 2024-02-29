myDict = {
    "Fast": "In a Quick Manner",
    "Parul":"A Coder",
    "Marks":[1,2,5],
    "anotherDict":{'Parul':'Player'}
}
print(myDict['Fast'])
print(myDict['Parul'])

# Marks Override
myDict['Marks']= [45,67]
print(myDict['Marks'])
print(myDict['anotherDict']['Parul'])