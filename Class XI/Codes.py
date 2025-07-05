#WAP to calculate the mean of five numbers.
'''a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
d=int(input("Enter the fourth number:"))
e=int(input("Enter the fifth number:"))
print("The mean number is" , (a+b+c+d+e/5))'''

#WAP to enter your name and age. 
'''a=input("Write your name:")
b=input("Write your age:")
print ("Your name is " , a, "and your age is" , b)'''

#WAP to calculate and display percentage of a student from a given marks of a student. 
'''a=int(input("Enter marks for first subject:"))
b=int(input("Enter marks for second subject:"))
c=int(input("Enter marks for third subject:"))
d=int(input("Enter marks for fourth subject:"))
e=int(input("Enter marks for fifth subject:"))
f=int(input("Enter the maximum possible mark in a single subject:"))
print("The average marks are", (a+b+c+d+e)/5)
print("The percentage of the student is",(a+b+c+d+e)*20/f)'''

#WAP to covert temperature from celcius scale to fahrenheit scale
'''a=int(input("Enter the temperature in celcius:"))
f= a*1.8 +32
print("The temperature in fahrenheit is" , f)'''

#WAP to calculate the area of a square and perimeter of a rectangle. 
'''a=int(input("Enter the side of the square:"))
print("The area of the square is" , a*a)

b=int(input("Enter the lenght of the rectangle:"))
c=int(input("Enter the breadth of the rectangle:"))
print("The perimeter of the rectangle is" , b*c)'''

#WAP to calculate the area of a triangle. 
'''a=int(input("What is the height of the triangle:"))
b=int(input("What is the breadth of the triangle:"))
print("The area of the triangle is" , a*b/2)'''

#WAP to calculate the area of a circle. 
'''a=int(input("Enter the radius of the circle:"))
print("The area of the circle is" , 2*3.14*a)'''

#WAP to calculate the compound interest of a given amount. 
'''a=eval(input("Enter the principle amount:"))
b=eval(input("Enter the rate of interest:"))
c=eval(input("Enter the time period:"))
d=a*(1+b/100)*c -a
print("The compound interest is" , d)'''

#WAP to display your name with '' Seperators. 
'''a=input("Enter your first name:")
b=input("Enter your surname:")
print("Your name is", a,b, sep="''")'''

#WAP to calculate the year is which you will turn 100 years old. 
'''a=int(input("Please enter your birth year:"))
print("The year in which you will turn 100 years old is" , a+100)'''

#WAP to convert time given in hours in minutes. 
'''a=eval(input("Please enter the time in hours"))
b=a*60
print("The time in minutes is" , b)'''

#WAP to calculate volume given in liters into milliliters. 
'''a=eval(input("Enter the volume in liters"))
print("The volume in milliliters is" , a*1000)'''

#WAP to calculate distance given in kilometers into meters. 
'''a=float(input("Enter the distance in kilometers:"))
b=a*1000 
print("The distance in meters is" , b)'''

#WAP to calculate time given in minutes into hours. 
'''a=float(input("Enter the time in minutes:"))
print("The time in hours is:" , a/60)'''

#WAP to calculate distance given in meters into kilometers. 
'''a=eval(input("Enter distance in meters:"))
b=a/1000
print("The distance in meters is:" , b)'''

#WAP to calculate the money given in rupees into paise. 
'''a=float(input("Enter the amount in rupees:"))
b= a*100
print("The amount in paise is" , b)'''

#WAP to print your name, age and class seperated by "/". 
'''a=input("Please write your name:")
b=int(input("Please enter your age:"))
c=input("Please enter your class")
print( a , b , c , sep="/")'''

#WAP to print quotient and reminder with dividend and divisor given. 
'''a=eval(input("What is the dividend?"))
b=eval(input("What is the divisor?"))
c=int(a//b)
print(c)'''

#WAP that accepts marks of 5 subjects and outputs the average. 
'''a=eval(input("Please enter marks of English:"))
b=eval(input("Please enter marks of German :"))
c=eval(input("Please enter marks of Sceince:"))
d=eval(input("Please enter marks of Maths :"))
e=eval(input("Please enter marks of Social Studies:"))
print("The average marks are" , (a+b+c+d+e)/5)'''

#WAP to input a number and print its first five multiples. 
'''a=eval(input("What is the number? :"))
print("The first 5 multiples of " , a, "are:" ,  a ,a*2 ,a*3 ,a*4 ,a*5)'''

#WAP to read details like name, age, class of a student and then print the details firstly in the same line then in the next line 
'''a=input("Please enter your name:")
b=int(input("Please enter your age in digits: "))
c= int(input("Please enter your class in digits: "))
print(a,b,c)
print(a,"\n", b , "\n", c)'''

#WAP to read three number in three variables and swap first two variables with the sums of the first and second , second and third respectively. 
'''a=int(input("Num 1: "))
b=int(input("Num 2: "))
c=int(input("Num 3: "))

a=a+b
b=b+c
print(a,b,c)''' 

#WAP to print the patterns. (Nested Loops)
'''for i in range(1,5):
    for j in range(1,i+1):
        print(j, end='')
    print()'''

'''for i in range(1,5):
    for j in range(0,i+1):
        print(j, end='')
    print()'''

#WAP to calculate a dog's age in dog's years.
'''a=eval(input("Please enter dog's age in human years"))
if a==1:
    print("Age of the dog in dog years is 10.5 years")
if a==2:
    print("Age of dog in dog years is 21 years")
else:
    print("Age of dog in dog years is", a*4+21)'''

#WAP to convert month name to a number of days. 
'''print("List of months:January, February, March, April, May, June, July, August, September, October, November, December")
a=input("Input name of the month:")
if a=="February":
    print("28/29 Days")
elif a== ("January, March, May, July, August, October, December"):
    print("31 days")
else:
    print("30 days")'''

#WAP to sum of two given integers. However, if the sum is between 15 to 20 it will return to 20. 
'''a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a+b==15 or a+b>15 or a+b==20 or a+b<20:
    print("The sum is 20")'''

#WAP to check wheather a triangle is equilateral, Scalene or Isosceles. 
'''a=eval(input("Please enter the first side: "))
b=eval(input("Please enter the second side: "))
c=eval(input("Please enter the third side: "))
if a==b==c:
    print("The triangle is an equilateral triangle")
elif a==b and a==c and b!=c:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")'''

#WAP to display astrological sign for given date of birth. 
'''day=int(input("Input birthday"))
month=input("Input month")
if month=='December':
    sign='Saggitarius' if(day<15) else'Capricorn'
elif month=='January':
    sign='Capricorn' if(day<15) else'Aquarius'
elif month=='February':
    sign='Aquarius' if(day<15) else'Pisces'
elif month=='March':
    sign='Pisces' if(day<15) else'Aries'
elif month=='April':
    sign='Aries' if(day<15) else'Taurus'
elif month=='May':
    sign='Taurus' if(day<15) else'Gemini'
elif month=='June':
    sign='Gemini' if(day<15) else'Cancer'
elif month=='July':
    sign='Cancer' if(day<15) else'Leo'
elif month=='August':
    sign='Leo' if(day<15) else'Virgo'
elif month=='September':
    sign='Virgo' if(day<15) else'Libra'
elif month=='October':
    sign='Libra' if(day<15) else'Scorpio'
elif month=='November':
    sign='Scorpio' if(day<15) else'Saggitarius'
print(sign)'''

#WAP to find the median of three values. 
'''a=eval(input("Input First Number"))
b=eval(input("Input Second Number"))
c=eval(input("Input Third Number"))
if a>b:
    if a<c:
        median=a
elif b>c:
    median=b
else:
    median=c
    if a>c:
        median=a
    elif b<c:
        median=b
    else:
        median=c
print("The median is", median)'''

#WAP to get next day of a given date.
'''a=int(input("Input a year"))
b=int(input("Input a month [1-12]"))
c=int(input("Input a day"))
print(a, b, c+1 , sep="-")'''

#WAP to display the sign of the Chinese Zodiac for the given year in which you were born.
'''year=int(input("Input your birth year"))
if (year-2000)%12==0:
    sign='Dragon'
elif (year-2000)%12==1:
    sign='Snake'
elif (year-2000)%12==2:
    sign='Horse'
elif (year-2000)%12==3:
    sign='Sheep'
elif (year-2000)%12==4:
    sign='Monkey'
elif (year-2000)%12==5:
    sign='Rooster'
elif (year-2000)%12==6:
    sign='Dog'
elif (year-2000)%12==7:
    sign='Pig'
elif (year-2000)%12==8:
    sign='Rat'
elif (year-2000)%12==9:
    sign='Ox'
elif (year-2000)%12==10:
    sign='Tiger'
else:
    sign='Hare'
print("Your Chinese Zodiac sign is", sign)'''

#WAP to convert a number from binary into it's equivalent decimal number. 
'''binary = int(input("Enter binary number: "))
num= 0
l=0
for i in range(len(str(binary))):
    digi = binary%10
    num = num + digi*2**l
    binary = binary//10
    l=l+1
print(num)'''

#WAP to print all prime numbers between 2 and 30.
'''for i in range(2,31):
    for j in range(2, 31):
        if i==j:
            continue
        else:
            if i%j == 0:
                break
            else: 
                continue
    else:
        print(i)
    #if y=="Number prime":
     #print(i)'''

'''for x in "banana":
    print(x)'''

'''a="Hello World"
print(len(a))'''

#WAP and write World is not enough and string the following:
'''s='World is not Enough'
print(len(s))
print(s[:5])
print(s[9:12])
print(s[9:19])
print(s[:4])
print(s[15:20])
print(s[-1:-6:-1])'''

#Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string. 
'''s=input("Enter a String: ")
if len(s)>=3:
    if s[-3:]=='ing':
        s +='ly'
    else:
        s +='ing'
else:
    print(s)'''

#WAP to perform all the mathematical operations of a calculator.
'''def calculator():
    print("Welcome to the Calculator!")
    print("Enter 'quit' to exit.")

    while True:
        operation = input("\nChoose an operation (+, -, *, /, %): ")

        if operation == 'quit':
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error! Division by zero is not allowed.")
                continue
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                print("Error! Division by zero is not allowed.")
                continue
        else:
            print("Invalid operation!")
            continue

        print(f"The result is: {result}")

calculator()'''

#WAP to accept a number and display the factorial of that number.

'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")'''

#WAP to check if a number is composite or not. 
'''a=int(input("Enter a number: "))
for i in range(2,a):
    if a%i==0:
        print("Number is Composite.")
        break
else:
    print("Number is not Composite")'''

#WAP to check whether a number is odd or even. 
'''a=eval(input("Enter the number"))
if a%2==0:
     print("Number is Even")
else: 
    print("Number is Odd")'''

#WAP to print the sum of squares of number 1-10.
'''a=0
for i in range(1,11):
    a=a +i**2
print(a)'''

#WAP to check whether a person is eligible to vote. 
'''a=int(input("Please Enter your Age: "))
if a>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")'''

#WAP to replace all occurrences of a with $.
'''s=input("Enter the String: ")
print(s.replace("a","$"))'''

#WAP to check if two strings are Anagrams. 
'''s=input("Enter First String: ")
t=input("Enter Second String: ")
if len(s)==len(t):
    for i in range(len(s)):
        if s[i] not in t:
            print("Strings are not Anagrams.")
            break
        elif t[i] not in s:
            print("Strings are not Anagrams.")
            break
    else:
        print("Strings are Anagrams.")
else:
    print("Strings are not Anagrams.")'''

#WAP to count the vowels in a string. 
'''s=input("Enter the String: ")
print(s.replace("","-"))'''

#WAP to calculate the number of words in a string and the number of characters present in a string. 
'''s=input("Enter the String: ")
print("The number of words: ", len(s.split()))
letters=0
for i in s:
    if i.isalpha():
        letters+=1
print("Number of Letters", letters)'''

#WAP to check whether a string is a palindrome or not.
'''s=input("Enter the String: ")
for i in range(len(s)):
    if s[i]!=s[-i-1]:
        print("The string is not a Palindrome.")
        break
else:
    print("The string is a Palindrome.")'''

#WAP to check whether a string is a panagram or not. 
'''s=input("Enter the String: ")
a="abcdefghijklmnopqrstuvwxyz"
for i in range(len(a)):
    if a[i] not in s:
        continue
    else: 
        print("The String is not a Panagram")
        break
else: 
    print("The String is a Panagram")'''

#WAP to enter the side of a square and print area and perimeter.
'''s=float(input("Enter the side of a square: "))
area=s**2
perimeter=s*4
print("Area of Square:", area)
print("Perimeter of Square:", perimeter)'''

'''lp=[]
ln=[]'''

#WAP to accept the names and marks in 5 subjects of a class of 5 students in a tuple. Display the name of each student along with it's total. 
'''x = 0
while x != 5:
    x += 1
    t1 = input("Enter name of student and marks (name)( tuple): ")
    t1 = eval(t1)  
    
    add = 0
    for i in range(len(t1)):
        if (t1[i], int):
            add += t1[i]
    
    print(f"Total marks: {add}")'''


#calculate and display the factorial od an inputted number
'''num=int(input("Enter the non negative number to take factorial of: "))
fact = 1
for i in range(num):
    fact = fact*(i+1)
print('Factorial of',num ,'-',fact)'''

# 1, 1 2, 1 2 3
'''for i in range(1,4):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''

# S=(1)+(1+2)+(1+2+3)
'''sum=0
n=int(input("How many terms?"))
for a in range(2,n+2):
    term=0
    for b in range(1,a):
        term+=b
    print('Term', (a-1),':',term)
    sum+=term
print('Sum of',n,'terms is:',sum)'''

#1, 3 3, 5 5 5 
'''n=10
for i in range(1,n+1,2):
    for j in range(0,i+1,2):
        print(i,end='')
    print()'''

# 5, 5 4, 5 4 3 
'''for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end='')
    print()'''

# 1, 1 2, 1 2 3 
'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

#Maximum value entered
'''n=int(input("Enter the first number:"))
max=n
for i in range(2,10):
    n=int(input("Enter the next number:"))
    if max<n:
        max=n
    print("Maximum value entered so far is:",max)'''

#Sum of the given series
'''sum=0
n=int(input("Enter the number of terms:"))
for i in range(2,n+2):
    term=0
    for b in range(1,i):
        term+=b
    print('Term', (i-1),':',term)
    sum+=term
print('Sum of',n,'terms is:',sum)'''

#Display factorial of a certain number
'''n=int(input("Enter the non negative number to get factorial of:"))
fact=1
for i in range(n):
    fact=fact*(i+1)
print('Factorial of',n,'is:',fact)'''

