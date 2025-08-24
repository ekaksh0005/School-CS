t1=tuple()
t2=tuple()
n=int(input("Enter no of values in t1:"))
for i in range(n):
    a=eval(input("Enter values of t1:"))
    t1=t1+(a,)
m=int(input("Enter no of values in t2:"))
for j in range(m):
    b=eval(input("Enter values of t2:"))
    t2=t2+(b,)
print(t1)
print(t2)
t1,t2=t2,t1
print(t1)
print(t2)
