import pickle
with open("items.dat","wb") as f:
    d={}
    c=input("Press Enter to Continue")
    while c.lower()!='n':
        x=input("Enter Student Admission No.: ")
        y=input("Enter Student Name: ")
        z=int(input("Enter Percentage: "))
        l=[]
        l.append(y)
        l.append(z)
        d[x]=l
        c=input("Continue? ")
    pickle.dump(d,f)

def copy_new():
    with open("items.dat","rb") as f:
        try:
            d=pickle.load(f)
        except:
            print("End of File!!")

    with open("new_items.dat","wb") as f:
        for i in d:
            if d[i][1]<=65:
                D={}
                D[i]=d[i]
                pickle.dump(D,f)

    with open("new_items.dat","rb") as f:
        try:
            while True:
                print(pickle.load(f))
        except:
            print("End of File!!")

copy_new()
