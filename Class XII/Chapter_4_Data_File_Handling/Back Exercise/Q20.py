f=open("WORK.txt")
a=f.read()
f.close()
l="asdfghjklqwertyuiopzxcvbnm"
u="QWERTYUIOPASDFGHJKLZXCVBNM"
for i in a:
    if i in l:
        with open("LOWER.txt","a") as f:
            f.write(i)
            f.close()
    elif i in u:
        with open("UPPER.txt","a") as f:
            f.write(i)
            f.close()
    elif i!=" ":
        with open("OTHER.txt","a") as f:
            f.write(i)
            f.close()
