f=open("WORK.txt")
Song=f.read()
f.close()
count=0
Song=Song.split()
x=Song.index("to")
y=Song.index("the")

for i in range(x,y+1):
    count+=1
print(count)
