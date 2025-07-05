def GCF(N1,N2):
    l1=[]
    l2=[]
    for i in range(1,N1+1):
        if N1%i==0:
            l1.append(i)
    for i in l1:
        if N2%i==0:
            l2.append(i)
    print("The Greatest Common Integer is",max(l2))
n1=int(input("Enter a Number: "))
n2=int(input("Enter a Number: "))

GCF(n1,n2)
