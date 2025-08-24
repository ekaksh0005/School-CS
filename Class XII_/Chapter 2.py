#17 Write a function that takes amt in dollars and dollar to rupee conversion price and then returns the amt converted
'''def conversion():
    a=int(input("Enter amt to be converted:"))
    b=int(input("Enter rate of conversion"))
    money=a*b
    print(money)
conversion()'''

#18 WRITE a func. to calc. the vol. of a box with default values
'''def volume():
    length=eval(input("Enter length of the box: "))
    width=eval(input("Enter Width of the box: "))
    height=eval(input("Enter Height of the box :"))
    vol=length*width*height
    print(vol)
volume()'''

#19 
'''def greatestcommondivisor():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    c=0
    for i in range(1,100):
        if a%i==0 and b%i==0:
            if i>c and i!=c:
                c=i
    print(c)
greatestcommondivisor()'''

#20
'''def multiply():
    x=1
    l=eval(input("Enter a list"))
    for i in l:
        x=x*i
    print(x)
multiply()'''

#21 
'''def factorial(n):
    s=1
    for i in range (1,n+1):
        s*=i
    print (s)
n=int(input('enter a number'))
factorial(n)'''

#22
'''def prime():
    a=0 
    num=int(input("Enter number: "))
    for i in range (2,num):
        if num%i !=0:
            print("Prime")
            break
        else:
            print("Composite")
            break
prime()'''

#23
'''def pallindrome(a):
    if a==a[::-1]:
        print ('pallindrome')
    else:
        print ('not a pallindrome')
a=input('enter a string')
pallindrome(a)'''

#24 
def hype(a):
    l=a.split('-')
    l.sort()
    s=''
    for i in l:
        s+=i+'-'
    print (s[0:-1])
a=input('enter a string')
hype(a)

#