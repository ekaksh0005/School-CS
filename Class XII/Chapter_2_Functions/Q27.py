def P_S(N):
    for i in range(2,N+1):
        a=0
        for j in range(2,i):
            if j%i==0:
                a=0
                break
            else:
                a=1
                break
        if a==1:
            print(i,": Number is Prime")
        else:
            print(i,": Number is NOT Prime")
l=eval(input("Enter a Number List: "))
P_S(l)
