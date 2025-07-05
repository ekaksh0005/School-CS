def Prime(l1):
    a=0
    for i in range(2,l1):
        if l1%i==0:
            a=0
            break
        else:
            a=1
    if a==1:
        print("Number is Prime")
    else:
        print("Number is NOT Prime")
l=eval(input("Enter a Number List: "))
Prime(l)

