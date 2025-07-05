import pickle
with open("sports.dat","wb") as f:
    while True:
        l=eval(input("Enter Data: "))
        pickle.dump(l,f)
        c=input("Continue: ")
        if c.lower()=='n':
            break

with open("sports.dat","rb") as f:
    with open("Athletics.dat","wb") as f2:
        try:
            while True:
                x=pickle.load(f)
                if x.lower=="athletics":
                    pickle.dump(x,f2)
        except:
            print("File Loading Completed!")

            
with open("Athletics.dat","rb") as f:
    try:
        while True:
            print(pickle.load(f))
    except:
        print("End of File!!")
