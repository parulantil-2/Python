# greeting="Good morning, "
# name= "Parul"
# # print(type(name))
# print(greeting  +  name)
# #  or
# #  concatenating two strings
# c= greeting + name 
# print(c)

name="Parul"
print(name[4])
# name[3]="d" DOES NOT WORK

print(name[0:3])   #Par
print(name[1:3])   #ar
# or
sl=name[1:4]
print(sl)          #aru
# same as[0:4]
print(name[:4])    #Paru
# same as[1:4]
print(name[1:])    #arul
print(name[-1])    #l
# same as[1:3]
print(name[-4:-1]) #aru

# slicing with skip values
d=name[1:4:1]    # arul >l will skip 
print(d)

d=name[1:4:2]    # arul >ul will skip 
print(d)

d=name[1:4:3]    # arul >rul will skip 
print(d)