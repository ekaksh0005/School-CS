#A list Num contains the elements: 3,25,13,6,35,8,14,45
#Write a program to swap the content wuth the next value divisible by 5 so that the resultant list will look like:
#25,3,13,35,6,8,45,14
l=eval(input('Enter an Input: '))
n=len(l)
for i in range(n):
    if l[i]%5==0:
        l[i-1],l[i]=l[i],l[i-1]
print(l)
