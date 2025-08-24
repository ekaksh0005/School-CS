import pickle
f=open('PATIENTS.dat','wb+')
n=[]
while True:
    PID=input("Enter patient ID")
    NAME=input("Enter name")
    DISEASE=input("Enter disease")
    n.append([PID,NAME,DISEASE])
    c=input("Continue?")
    if c.lower()=='n':
        break
pickle.dump(n,f)
f.flush()
f.seek(0)
count=0
x=pickle.load(f)
print(x)


f=open('PATIENTS.dat','wb+')
for i in x:
    if i[2] =='COVID-19':
        print(i[2])
        count+=1

print("No of patient with COVID19 are:",count)
