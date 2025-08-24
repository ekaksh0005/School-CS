def DISPEMP():
    import csv
    count=0
    f=open('emp.csv','r+',newline='\n')
    a=csv.reader(f)
    for i in a:
        if int(i[2])<5000:
            count+=1
            print('No of employees earning less than 5000 are:',i,count)

DISPEMP()
