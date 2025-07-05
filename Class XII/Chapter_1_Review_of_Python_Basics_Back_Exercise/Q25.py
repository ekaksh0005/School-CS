#
d=eval(input('Enter a Dictionary: '))
x=input('Enter the name of the student to be deleted: ')

if x in d:
    del d[x]
print(d)
