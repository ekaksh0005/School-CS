count=0
def count_Dwords():
    f=open('Details.txt','r')
    l=f.readlines()
    for i in l:
        if i[-1].isdigit():
            count+=1
print("Digit ending chars are:",count)

            
