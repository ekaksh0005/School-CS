CustomerName=[]
while True:
    name=input("Enter name of customer")
    CustomerName.append(name)
    c=input("Continue?")
    if c.lower()=='n':
        break
def AddCustomer(CustomerName):
    name=input("Enter name")
    CustomerName.append(name)
def DeleteCustomer(CustomerName):
    CustomerName.pop()

c=input("1. Add, 2. Delete")
if c=='1':
    AddCustomer(CustomerName)
if c=='2':
    DeleteCustomer(CustomerName)
