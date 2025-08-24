a=0
f=open('Poem.txt','r')
l=f.readlines()
for i in l:
    half=i.split()
    for j in half:
        if j.isupper():
            a+=1
print("Number of uppercase:",a)
f.close()
