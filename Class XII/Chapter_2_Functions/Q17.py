def Void(M):
    print(M*85.68)
def Non_Void(M):
    x=M*85.68
    return int(x)
m=float(input("Enter the Money in USD: "))
Void(m)
print(Non_Void(m))
