#Write a Program to shift elements of a list so that the first element moves to second index and second index moves to the third index, and so on, and the last element shifts to the first position.
#Suppose the list is [10,20,30,40]
#After shifting, it should look like: [40,10,20,30]
l=eval(input('Enter an Input: '))
x=l[-1]
l.pop(-1)
l.insert(0,x)
print(l)
