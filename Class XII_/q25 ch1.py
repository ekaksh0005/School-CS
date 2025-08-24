d1=dict()
n=int(input("Enter the number of students:"))
for i in range(n):
    std=input("Enter name of student:")
    perc=input("Enter percentage:")
    d1[std]=perc

dt=input("Enter name of student to delete:")
del d1[dt]
print(d1)
