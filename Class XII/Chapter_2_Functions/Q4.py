def pattern(N):
    for i in range(1,N+1):
        for j in range(i):
            print("*",end=" ")
        print()
n=int(input("Enter a Number: "))
pattern(n)
