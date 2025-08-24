import pickle
f=open('abc.dat','wb+')
n=[]
while True:
    l=eval(input("Enter data:"))
    n.append(l)
    c=input("continue?")
    if c.lower()=='n':
        break
pickle.dump(n,f)
f.flush()
f.seek(0)
x=pickle.load(f)
print(x)
