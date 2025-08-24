import pickle
f=open('Employee.dat','wb+')
n=[]
while True:
    Name=input("Enter name of employee")
    Salary=int(input("Enter salary of employee"))
    DOB=input("Enter date of birth")
    n.append([Name,Salary,DOB])
    c=input("Continue?")
    if c.lower()=='n':
        break
pickle.dump(n,f)
f.flush()
f.seek(0)
x=pickle.load(f)
for i in x:
    print(i)
    if i[0][0]=='p' or i[0][0]=='P':
        (i[1])+=2000
        print(x)
