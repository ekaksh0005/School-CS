f=open('Test-1.txt')
mytext=f.read()
f.seek(0)
mytextline=f.readlines()
f.close()
print(mytext,mytextline,sep='\n')
#Number of vowels in entire text file
vowels='aeiouAEIOU'
count=0
for i in mytext:
    if i in vowels:
        count+=1

print(count)
#Number of words in entire text file
l=mytext.split()
count2=0
for i in l:
    count2+=1
print(count2)
#Number of Words in Each Line
f=open('Test-1.txt')
mytextlines=f.readlines()
f.close()
for i in mytextlines:
    x=[]
    count3=0
    x=i.split()
    for j in x:
        count3+=1
    print(count3)
#For Line Starting with Vowel
for i in mytextlines:
    if i[0] in vowels:
        x=[]
        count3=0
        x=i.split()
        for j in x:
            count3+=1
        print(count3)

