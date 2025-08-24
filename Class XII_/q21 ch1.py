list1=[3,25,13,6,35,8,14,45]
for i in range(len(list1)):
    if list[i]%5==0:
        list1[i],list1[i-1]=list1[i],list1[i+1]
    print(list1)
