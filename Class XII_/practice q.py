import pickle
f=open('abc.dat','wb')
while True:
    l=eval(input('Enter data'))
    pickle.dump(l,f)
    c=input('continue?')
    if c.lower()=='n':
        break

f.flush()
f.seek(0)
f=open('abc.dat','rb')
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print("End of file")
