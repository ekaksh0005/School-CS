d={}
n=int(input('Enter No. of Customers: '))
for i in range(n):
    name=input('Enter name of Customer: ')
    item=input('Enter item bought: ')
    cost=eval(input('Enter the cost of item: '))
    ph_no=int(input('Enter contact no.: '))
    d[name]=[item,cost,ph_no]
print('Name','\t','Item','\t','Cost','\t','Contact Number')
for i in d:
    print(i,'\t',d[i][0],'\t',d[i][1],'\t',d[i][2])
