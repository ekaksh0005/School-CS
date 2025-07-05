b=input("Enter a File Name/Path to read from: ")
with open(b,"r") as f:
    MyS=f.read()
    f.close()

a=input("Enter a New Name for Location on Desktop: ")

with open(a,"w") as F:

    F.writelines(MyS)
    F.close()
    
