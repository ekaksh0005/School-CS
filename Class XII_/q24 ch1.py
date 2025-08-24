cls=dict()
n=int(input("Enter number of classes:"))
for i in range(n):
    sec=input("Enter section:")
    tch=input("Enter teachers name:")
    cls[sec]=tch
print(cls)
cl=input("Enter a section name:")
if cl in cls.keys():
    print(cls[tch])
