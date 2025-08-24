def fileout():
    f=open("STRS.txt",'w')
    while True:
        data=input('Enter any things:-')
        f.write(data+'\n')
        user=input("Do you wnat to enter more data?")
        if user=='No' or user=='no':
            break
    f.close

fileout()
