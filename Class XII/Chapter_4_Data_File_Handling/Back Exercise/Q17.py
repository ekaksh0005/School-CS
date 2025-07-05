f=open("WORK.txt")
x=f.read()
f.close()
count=0
y="QWERTYUIOPASDFGHJKLZXCVBNM"
for i in x:
    if i in y:
        count+=1
print(count)
