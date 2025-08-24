t1=tuple()
n=int(input("Enter number of values in a tuple:"))
for i in range(n):
    a=eval(input("Enter a value:"))
    t1=t1+(a,)
for i in t1:
    print(i)
print("Max value in the tuple is:",max(t1))
print('Min value of the tuple is:',min(t1))
