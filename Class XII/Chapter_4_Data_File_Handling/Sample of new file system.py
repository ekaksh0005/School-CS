import pickle as p
with open("Test.dat","wb") as f:
    while True:
        l=eval(input("Enter Data: "))
        p.dump(l,f)
        c=input("Continue: ")
        if c.lower()=='n':
            break

with open("Test.dat","rb") as f:
    try:
        while True:
            print(p.load(f))
    except:
        print("End of File!!")
