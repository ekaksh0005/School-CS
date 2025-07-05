l=[]
for i in range(1,31):
    l.append(i**2)
x=l[:5]+l[-1:-6:-1]

print(x)
