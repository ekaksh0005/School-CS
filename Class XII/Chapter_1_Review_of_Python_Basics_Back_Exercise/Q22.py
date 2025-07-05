#Write a program to accept values from a user in a tuple. Add a tuple to it and display its elements one by one. Also display its maximum and minimum value.
n=int(input('Enter No. of Elements: '))
t=()
for i in range(n):
    x=eval(input('Enter a Value: '))
    t+=x,
print(t)
for i in t:
    print(i)
print(max(t),min(t),end='\n')
