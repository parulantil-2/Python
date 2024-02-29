# myDict ={
# "pankha": "fan",
# "Dabba":"Box",
# "Vastu":"Item"
# }
# print("options are ", myDict.keys())
# a= input("enter hindi word\n")
# # print("the meaning of the word is : ", myDict[a])

# # below line will not throw an error if the key is not present
# print("the meaning of the word is : ", myDict.get(a))


# n1 = int(input("enter number 1"))
# n2 = int(input("enter number 2"))
# n3 = int(input("enter number 3"))
# n4 = int(input("enter number 4"))
# n5 = int(input("enter number 5"))
# n6 = int(input("enter number 6"))
# n7 = int(input("enter number 7"))
# n8 = int(input("enter number 8"))
# s ={n1,n2,n3,n4,n5,n6,n7,n8}
# print(s)


s={18 , "18",18.1}
print(s)


# in set 20 and 20.0 are same
s={20, 20.0,"20"}
print(len(s))


s={}
print(type(s))


# favLang = {}
# a= input("enter your favourite language shumbham\n")
# b= input("enter your favourite language ankit\n")
# c= input("enter your favourite language somali\n")
# d= input("enter your favourite language harshita\n")
# favLang['shubham'] = a
# favLang['ankit'] = b
# favLang['somali'] = c
# favLang['harshita'] = d
# print(favLang)


favLang = {}
a= input("enter your favourite language shumbham\n")
b= input("enter your favourite language ankit\n")
c= input("enter your favourite language shubham\n")
d= input("enter your favourite language harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['shubhaam'] = c
favLang['harshita'] = d
print(favLang)


# answer 9 no 
# value cannot be changed inside the tuple
# no