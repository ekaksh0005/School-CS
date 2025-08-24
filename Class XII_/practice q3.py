import pickle
f=open('sports.dat','wb+')
info=[]
while True:
    event=input("Enter event name:")
    players=input("Enter no of players:")
    data=[event,players]
    info.append(data)
    c=input('Continue?')
    if c.lower()=='n':
        break
pickle.dump(info,f)

f.close()
f=open('sports.dat','rb+')
x=pickle.load(f)
print(x)

f=open('Athletics.dat','wb+')
for i in x:
    if i=='Athletics' or i=='athletics':
        pickle.dump(i,f)
f.flush()
f.seek(0)
f=open('Athletics.dat','rb+')
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print('end of code')
