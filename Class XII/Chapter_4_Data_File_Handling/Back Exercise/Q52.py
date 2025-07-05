import csv
with open("Groceries.csv","a",newline='') as f:
    l=eval(input("Enter The ROWS: "))
    a=csv.writer(f)
    a.writerows(l)
    f.close()
    
with open("Groceries.csv","r",newline='') as f:
    a=csv.reader(f)
    next(a) #if we don't want to count the first row, and shift the pointer to new row
    for i in a:
        print(i)
