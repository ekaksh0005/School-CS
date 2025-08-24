import pickle
f=open('items.dat','wb+')
n={}
while True:
    item_id=input("Enter item id")
    item_name=input("Enter item name")
    amount=int(input("Enter amount"))
    n[item_id]=[item_name,amount]
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
    
f=open('new_items.dat','wb+')
for i in x:
    if x[i][1]>1000:
        pickle.dump(x[i],f)
        f.flush()
f.seek(0)
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print('end of file')
    
