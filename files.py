# use oprn function to read the content of the file
# by default mode is r
# f= open('sample.txt')
f= open('sample.txt','r')
data=f.read()
# read only 5 characters from file
data=f.read(5)
print(data)
f.close()
