import requests

with open('internallink.txt', '+r') as file:
    a=file.readlines()
b=[]
for i in range(len(a)):
    a1 = a[i][:len(a[i])-1]
    b.append(a1)

# print(b)
c =[]
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][-1:-3] == 'php':
            c.append(b[i])
print(c)