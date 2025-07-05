#Write a program to multiply an element by 2 if it is at an odd index for a given list containing both numbers and strings
l=eval(input("Enter an Input: "))
n=len(l)
for i in range(n):
    if i%2!=0:
        l[i]=l[i]*2

print(l)
