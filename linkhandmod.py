
b=[]
with open('internallink.txt','+r') as r:
    a = r.readlines()

for i in range(len(a)):
    if '.php' in a[i]:
        clean=a[i].replace("\n","")
        print(clean)
        b.append(clean)
print(b)