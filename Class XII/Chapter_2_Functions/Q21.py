def Multiply(l1):
    p=1
    for i in range(1,l1+1):
        p*=i
    return p
l=eval(input("Enter a Number List: "))
print("The Factorial of",l,"is",Multiply(l))

