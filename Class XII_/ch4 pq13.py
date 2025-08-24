import pickle
f=open('game.dat','wb+')
n=[]
while True:
    game_name=input("Enter name of game")
    participants=input("Enter no of participants")
    n.append([game_name,participants])
    c=input('Continue?')
    if c.lower()=='n':
        break
pickle.dump(n,f)
f.flush()
f.seek(0)
x=pickle.load(f)
print(x)

f=open('basket.dat','wb+')
for i in x:
    if i[0]=='Basketball':
        pickle.dump(i,f)
f.flush()
f.seek(0)

try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print('EOL')
