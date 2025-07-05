def Sorter(s):
    l1=s.split("-")
    l1.sort()
    for i in l1:
        print(i,end="-")
S=input("Enter a input: ")
Sorter(S)
