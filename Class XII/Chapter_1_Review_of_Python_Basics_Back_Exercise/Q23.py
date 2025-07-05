#Write a program to input any values for two tuples. Print it, interchange it and then compare them.
t1=eval(input("Enter the Input: "))
t2=eval(input("Enter the Input: "))
print(t1,t2)
x=t2
t2=t1
t1=x
print(t1,t2)

if t1<t2:
    print('t2 is greater')
else:
    print('t1 is greater')
