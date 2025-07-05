import csv
with open("book1.csv","r+",newline='') as f:
    a=csv.reader(f)
    next(a)
    for i in a:
        print(i)
