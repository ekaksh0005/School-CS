s=input('Enter a string: ')
j=''
x=''
l=s.split()
for i in l:
    j=i[0].upper()+i[1:-1]+i[-1].upper()
    x+=j+' '
print(x)
