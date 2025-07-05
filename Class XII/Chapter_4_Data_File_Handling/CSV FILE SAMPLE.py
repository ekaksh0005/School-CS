import csv
with open("book1.csv","r+",newline='') as f: #newline is for default argument that it will directly go to new line without creating a extra empty row
    a=csv.reader(f)
    next(a) #if we don't want to count the first row, and shift the pointer to new row
    for i in a:
        print(i)

    a=csv.writer(f)
    l=eval(input("Enter a Value: "))
    a.writerow(l)
