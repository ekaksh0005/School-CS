def Multiply(l1):
    p=1
    for i in l1:
        p*=i
    return p
l=eval(input("Enter a Number List: "))
print("The Product of Elements of given list is",Multiply(l))
