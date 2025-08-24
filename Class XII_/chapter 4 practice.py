#Q16
'''f=open('practice1.txt','r')
l=f.read()
x=l.split()
count1=x.count('to')
count2=x.count('the')
print('The no. of times to is there',count1)
print('The no. of times the is there',count2)'''

#Q17
'''f=open('practice1.txt','r')
l=f.read()
count=0
for i in l:
    if i.isalpha()==True:
        if i.isupper()==True:
            count=count+1
print(count)'''

#Q18
'''file1=input('Enter the first file.')
file2=input('Enter the second file.')
x=open(file1,'r')
y=open(file2,'w')
copy=x.read()
print(copy)
y.write(copy)
y.close()
x.close()'''

#Q19
'''file1=input('Enter the first file.')
file2=input('Enter the second file.')
x=open(file1,'r')
data=x.read()
list1=data.split()
y=open(file2,'a')
for i in data:
    y.write(i)
y.close()
x.close()'''

#Q20
'''file1=input('Enter the first file.')
x=open(file1,'r')
data=x.read()
upper=open('UPPER.txt','w')
lower=open('LOWER.txt','w')
other=open('OTHER.txt','w')
for i in data:
    if i.isupper():
        upper.write(i)
    elif i.islower():
        lower.write(i)
    else:
        other.write(i)
x.close()
upper.close()
lower.close()
other.close()'''

#Q22
'''file1=input('Enter the first file.')
x=open(file1,'r')
data=x.readlines()
count=0
for i in data:
    if i.startswith('A') or i.startswith('a'):
        count=count+1
print(count)'''

'''x=open('practice1.txt','w+')
x.write('board exams 2025')
x.seek(10)
x.write('siuhgvihd')
x.flush()'''

'''x=open('practice1.txt','r')
y=x.read()
list1=y.split()
for i in list1:
    if len(i)>5:
        print(i)
x.close() '''

'''x=open('practice1.txt','r')
y=x.read()
list1=y.split()
for i in list1:
    if i[-1].isdigit():
        print(i)
x.close()'''

'''import pickle
f=open('abc.dat','wb')
while True:
    l=eval(input('Enter data.'))
    pickle.dump(l,f)
    c=input('continue?')
    if c.lower()=='n':
        break
f.close()
f=open('abc.dat','rb')
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print('End of file')'''

'''import pickle
f=open('abc.dat','wb')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
f=open('abc.dat','rb')
x=pickle.load(f)
print(x)'''

#Q15
'''import pickle
f=open('sports.dat','wb')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
k=open('Athletic.dat','wb+')
list2=[]
for i in list1:
    if i[0]=='Athletics':
        list2.append(i)
pickle.dump(list2,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x)'''
        
#Q38
'''import pickle
f=open('items.dat','wb')
dict1={}
while True:
    l=eval(input('Enter data.'))
    itemid=input('Enter key')
    dict1[itemid]=l
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(dict1,f)
list1=[]
k=open('newitems.dat','wb+')
for i in dict1.values():
    if i[-1]>=1000:
          list1.append(i)
pickle.dump(list1,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x) '''

#Q43
'''import pickle
f=open('student.dat','wb')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
k=open('lessthan40.dat','wb+')
list2=[]
for i in list1:
    if i[-1]<40:
        list2.append(i[0])  
pickle.dump(list2,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x) '''

#Q44
'''import pickle
f=open('product.dat','wb')
l=eval(input('Enter a list of dictionaries.'))
pickle.dump(l,f)
f.flush()
k=open('product.dat','rb+')
pc=int(input('Enter the product code of the item you want to change.'))
s=int(input('Enter the new stock value.'))
list2=pickle.load(k)
for i in range(len(list2)):
    if list2[i]['prod_code']==pc:
        list2[i]['stock']=s
print(list2)
k.seek(0)
pickle.dump(list2,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x)''' 

#Q45
'''import pickle
f=open('Student.dat','wb')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
k=open('lessthan65.dat','wb+')
list2=[]
for i in list1:
    if i[-1]<65:
        list2.append(i)
pickle.dump(list2,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x)'''


'''import pickle
f=open('patients.dat','wb')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
count=0
k=open('covid.dat','wb+')
list2=[]
for i in list1:
    if i[-1]=='COVID19':
        list2.append(i)
        count=count+1
pickle.dump(list2,k)
k.flush()
k.seek(0)
x=pickle.load(k)
print(x)
print(count)'''

'''import pickle
f=open('players.dat','wb+')
list1=[]
while True:
    l=eval(input('Enter data.'))
    list1.append(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
pickle.dump(list1,f)
list2=[]'''
#(i)
'''def whoaaa():
    global list1
    for i in list1:
        if i[1].startswith('A'):
            list2.append(i)
    return list2
print(whoaaa())'''
#(ii)
'''count=0
def country():
    a=input('Enter a country name.')
    for i in list1:
        if i[2]==a:
            global count
            count=count+1
    return count
print(country())'''
#(iii)
'''crazyyyy=eval(input('Enter data.'))
pickle.dump(crazyyyy,f)
f.flush()
f.seek(0)
x=pickle.load(f)
print(x)'''
        
'''import csv
f=open('practice1.csv','r+',newline='')
a=csv.reader(f)
for i in a:
    print(i)
a=csv.writer(f)
l=eval(input('Enter data'))
a.writerow(l)
f.close()'''

'''import csv
f=open('practice1.csv','r+',newline='')
a=csv.reader(f)
for i in a:
    print(i)
a=csv.writer(f)
while True:
    l=eval(input('Enter data.'))
    a.writerow(l)
    c=input('continue?')  
    if c.lower()=='n':
        break
f.close()'''

'''import csv
f=open('practice1.csv','r+',newline='')
a=csv.reader(f)
for i in a:
    if i[0].startswith('A'):
        print(i)
f.close()'''

'''import csv
f=open('practice1.csv','r+',newline='')
a=csv.reader(f)
next(a) #to skip the column headings.
count=0
for i in a:
    count=count+1
print(count)
f.close()'''


