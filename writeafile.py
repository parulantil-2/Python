f=open('another.txt','w')
f.write("please write this to the file")
f.close()

# want to add content to another.txt open the file in apppend mode

f=open('another.txt','a')
f.write("i am appending")
f.close()