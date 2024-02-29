def remove_and_split(string,word):
     newStr = string.replace(word, "")
     return newStr.strip()


this = "    Hello how are you     "
n = remove_and_split(this, "Hello")
print(n)

# print(this)
# print(this.strip())

# strip function-removes extra spaces . 
 