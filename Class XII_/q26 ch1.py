info={}
n=int(input("Enter the number of customers:"))
for i in range(n):
    name=input("Enter the name of customer:")
    itm=input("items bought")
    cost=input("Enter cost")
    phone=input("phone number")
    info[name]=[itm,cost,phone]
    print(info)
