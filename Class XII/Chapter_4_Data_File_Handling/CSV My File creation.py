import csv
with open("book1.csv","w+",newline='') as f:
    a=csv.writer(f)
    l=eval(input("Enter a Value: "))
    a.writerow(l)
