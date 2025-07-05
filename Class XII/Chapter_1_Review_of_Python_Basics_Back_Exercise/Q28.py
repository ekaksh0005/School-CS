s=input('Enter a string: ')
x=''
for i in s:
    if i not in x:
        x+=i
print(x)
