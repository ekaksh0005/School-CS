#19 WAP to count the frequency of an element in a list 
'''list1=input("Enter list:")
count1=input("Enter element to be counted:")
print("The frequency is",count1.count())'''

#20 WAP to shift elements of a list so that the first element occupies the second index , second element
# moves to the third index and the last element shifts to the first position
'''list1=[10,20,30,40]
list1.pop()
list1.insert()
print(list1)'''

#21 WAP to calculate a dog's age in dog's years.
'''a=eval(input("Please enter dog's age in human years"))
if a==1:
    print("Age of the dog in dog years is 10.5 years")
if a==2:
    print("Age of dog in dog years is 21 years")
else:
    print("Age of dog in dog years is", a*4+21)'''

#22 WAP to check wheather a triangle is equilateral, Scalene or Isosceles. 
'''a=eval(input("Please enter the first side: "))
b=eval(input("Please enter the second side: "))
c=eval(input("Please enter the third side: "))
if a==b==c:
    print("The triangle is an equilateral triangle")
elif a==b and a==c and b!=c:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")'''

#23 WAP to display astrological sign for given date of birth. 
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

#24 WAP to display the sign of the Chinese Zodiac for the given year in which you were born.
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

#25 WAP to perform all the mathematical operations of a calculator.
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

        print("The result is: {result}")

calculator()'''

#26 WAP to accept a number and display the factorial of that number.

'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")'''

#27 WAP to check whether a string is a panagram or not. 
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

#28 WAP to calc. length of a string
'''str1= 'Python Program'
print("The length of the string is ", len(str1))'''

#29 WAP to change all occurences except the first one to $
'''str1='restart'
char=str1[0]
str1=str1.replace(char,'$')
result=char + str1[1:]
print("The modified String is", result)'''

#30 WAP to remove nth index char
'''str1='Python'
index=[0,3,5]
for n in index:
    first=str1[:n]
    last=str1[n+1:]
    new=first + last
print("Removing index",n ":", new)'''

#31 WAP to input n classes and names of class teacher to store in a dictionary and display them.
'''dict1={}
n=int(input("Enter the number of classes you want to list:"))
for i in range(n):
    classname=input("Please enter name of the class: ")
    teachername=input("Please enter name of class teacher: ")
    dict1[classname]=teachername
class_name_dict=input("Enter class name to be found: ")
print(dict1[class_name_dict])'''

#32 WAP to store student names and their percentage and display them.
'''dict1={}
n=int(input("Enter the number of students percentage you want to store: "))
for i in range (n):
    studentname=input("Enter name of student: ")
    percentage=eval(input("Enter percentage for student"))
    dict1[studentname]=percentage
student_name=input("Enter name of student to be found: ")
print(dict1[student_name])'''

#33 WAP to store groceries bought by each person in a dictionary and display it. 
'''dict1={}
n=int(input("Enter the number of person you want to store for: "))
for i in range(n):
    name=input("Enter person name: ")
    item=input("Enter the item you bought: ")
    cost=eval(input("Enter cost of the item bought: "))
    number=int(input("Please enter your phone number: "))
    dict1[name]=item,cost,number
person_name=input("Enter the name of person you want to see: ")
print(dict1[person_name])'''

#34 WAP to store students info like adm no. , class, section, name and percentage. Display it afterwards
dict1={}
n=int(input("Enter number of students you want to log: "))
for i in range(n):
    Adm=int(input("Enter Admission number: "))
    Name=input("Enter name of student: ")
    section=input("Enter students class and section: ")
    percentage=eval(input("Enter percentage of student: "))
    dict1[Adm]=Name,section,percentage
adm_number=int(input("Enter Student's Admission number to be searched: "))
print(dict1[adm_number])