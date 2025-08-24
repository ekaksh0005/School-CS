import pickle
f=open('STUDENT.dat','wb+')
n=[]
while True:
    S_Admno=input("Enter admission number")
    S_Name=input('Enter name')
    Percentage=float(input("Enter percentage"))
    n.append([S_Admno,S_Name,Percentage])
    pickle.dump(n,f)
    c=input("Continue?")
    if c.lower()=='n':
        break
f.flush()
f.seek(0)
try:
    while True:
        x=pickle.load(f)
except:
    print(x)

f=open('STUDENT.dat','wb+')
for i in x:
    if i[2]<65:
        pickle.dump(x,f)
        f.flush()
f.seek(0)
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print("End of file")
    
