def remedial():
    import pickle
    f=open('Student.dat','wb+')
    n={}
    while True:
        Name=input("Enter name of student:")
        Marks=int(input("Enter marks of student:"))
        n[Name]=[Marks]
        pickle.dump(n,f)
        c=input("Continue?")
        if c.lower()=='n':
            break
    f.flush()
    f.seek(0)
    try:
        while True:
            x=pickle.load(f)
            print(x)
    except:
        print("end of file")
    f=open('Student.dat','wb+')
    for i in x:
        if x[i][0]<40:
            pickle.dump(i,f)
            f.flush()
    f.seek(0)
    try:
        while True:
            x=pickle.load(f)
            print(x)
    except:
        print("End of file")
    
remedial()
