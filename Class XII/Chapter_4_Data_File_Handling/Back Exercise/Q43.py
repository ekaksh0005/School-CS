import pickle
with open("Students.dat","wb") as f:
    d={}
    c=input("Press Enter to Continue")
    while c.lower()!='n':
        x=input("Enter Student Name: ")
        l=int(input("Enter Student Marks: "))
        d[x]=l
        c=input("Continue? ")
    pickle.dump(d,f)

def copy_new():
    with open("Students.dat","rb") as f:
        try:
            d=pickle.load(f)
        except:
            print("End of File!!")

    with open("Remedial.dat","wb") as f:
        for i in d:
            if d[i]<=40:
                pickle.dump(i,f)

    with open("Remedial.dat","rb") as f:
        try:
            while True:
                print(pickle.load(f))
        except:
            print("End of File!!")

copy_new()
