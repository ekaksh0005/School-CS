f=open("arjn.txt",'r')
count=0
l=f.readlines()
for i in l:
    if i[0]=='A' or i[0]=='a':
        count+=1
print('number of lines:',count)
f.close()
