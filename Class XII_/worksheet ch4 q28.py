def DISPEMP():
    import csv
    f=open('emp.csv','r+',newline='\n')
    a=csv.reader(f)
    for i in a:
        if int(i[2])>=4000:
            print(i)

DISPEMP()
