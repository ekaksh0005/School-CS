#Q1
def Words(F):
    mytext=F.readlines()
    f.seek(0)
    mytest=F.read()
    F.close
    for i in mytext:
        x=[]
        x=i.split()
        if len(x)==5:
            print(i)
    print(mytest)

f=open("New_Text.txt")
Words(f)
