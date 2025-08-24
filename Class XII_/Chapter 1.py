#pg 1.71
#18. WAP to multiply an element by 2 if it is an odd index for a given list containing both numbers and strings
'''list1=eval(input("Enter no."))
for i in range (0,len(list1)):
    if i%2!=0:
        list1[i]=list1[i]*2
print(list1)'''

#19 WAP to count the frequency of an element in a list
'''list1=eval(input("Enter list"))
element=int(input("Enter element"))
print(list1.count(element))'''

#20 WAP to shift the elements of a list so that the first element moves to the second index and second index moves to third
#and so on, and the last element shits into first position
'''l=[10,20,30,40]
x=l.pop()
l.insert(0,x)
print(l)'''

#21 A list num contains elements: 3,25,13,6,35,8,14,45
#WAP to swap the content with the next value divisible by 5
'''list1=[3,25,13,6,35,8,14,45]
for i in range(len(list1)):
    if list[i]%5==0:
        list1[i],list1[i-1]=list1[i],list1[i+1]
    print(list1)'''

#22 WAP to accept values from a user in a tuple. Add a tuple to it and display its elements one by one. Also display min and max
'''t1=eval(input("Enter no."))
t2=eval(input("enter no."))
t=t1+t2
for i in t:
    print(i)
print("Max value is",max(t))
print("Min value is",min(t))'''

#23 WAP to input any values for two tuples. Print it, Interchange it and then compare them.
'''t1=eval(input("Enter tuple:"))
t2=eval(input("Enter other tuple:"))
t1,t2=t2,t1
if t1>t2:
    print("t1>t2")
else:
    print("t2>t1")'''

#24 WAP to input 'n' classes and names of class teachers to store them in a dictionary and display it. Also accept a particular
#class from user and display name of class teacher of that class
'''dict1={}
n=int(input("Enter number of classes to be logged:"))
for i in range(n):
    classname=input("Enter class name:")
    teachername=input("Enter name of class teacher")
    dict1[classname]=teachername
class_name=input("Enter class to be searched:")
print(dict1[class_name])'''

#25 WAP to store student names and their percentage in a dictionary and delete a particular student name from dictionary
#Also display after deletion
'''dict1={}
n=int(input("Enter number of students to be logged:"))
for i in range(n):
    studentname=input("Enter name of student:")
    percentage=input("Enter percentage of said student:")'''
    

