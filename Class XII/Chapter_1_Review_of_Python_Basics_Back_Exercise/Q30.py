s=input('Enter a string: ')
l=s.split(' ')
l2=[]
for i in range(len(l)):
    x=l.count(l[i])
    l2.append(x)
    max1=max(l2)
    max2=l2[0]
for i in range(len(l2)):
    if l2[i]>max2 or l2[i]<max2:
        max2=l2[i]
print(l[max2])
