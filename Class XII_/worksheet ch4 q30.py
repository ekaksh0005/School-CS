def SNAMES():
    import csv
    count=1
    f=open('emp.csv','r+',newline='\n')
    a=csv.writer(f)
    for i in a:
        if i[1][0]=='s' or i[1][0]=='S':
            print(i)
            count+=1
        print('No of names starting from S are:',count)
            
SNAMES()
