x=int(input('Enter a number: '))
s=0
while x>0:
    b=x%10
    s+=b
    x=x//10
print(s)
