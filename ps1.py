f = open('poems1.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else :
    print("twinkle in not present")
f.close()
