'''f=open('test.txt','r+')
f.write(" The Party was awsome, his house had many rooms \n")
f.write("He had a lot of guests attending the party \n")
f.write("His house was near Ishowspeed's house and also next to Kai Cenat's house. \n")
f.write("His house was worth a whopping 50 Million Dollars \n")
f.seek(0)
x=f.readlines()
print(x)
f.close()'''

#Open file in w+ mode, write something in the file, then save it without closing

'''with open('ekaksh.txt','w+') as f:
    a=f.writelines(["Hello this shishtam works \n", "So now that this works, I wanted to share that i recently went to my friedns party and turns out he had drugs !!! \n","I did not take any drugs because i wanted a life of my own and wanteed to do something in my nonexistent life \n" ])
    f.flush()
    print(a)'''

#Open a file in w mode, wirte anything and use close function

'''with open('Hello.txt','w') as f:
    a=f.write("Hello another world, how are you!! \n")
print(f.closed)'''

#By importing pickle

'''import pickle
f=open('cars.dat','wb')
while True:
    l=eval(input("Enter data:"))
    pickle.dump(l,f)
    c=input("Do you wish to continue? y/n")
    if c.lower()=='n':
        break
f.close()
f=open('cars.dat','rb')
try:
    while True:
        x=pickle.load(f)
        print(x)
except:
    print("End of File :)")'''


#WAP with 'sports.dat' which contains info as: EventName, Participant. Write a function that would read contents from sports file and create a file named Athletics copying records from sports file
'''import pickle
d={}
n=int(input("Enter the number of events you want to log: "))
for i in range(n):
    Event=input("Enter event name: ")
    Part=int(input("Enter number of participants"))
    dict[i]=Event
f=open("sports.dat","wb")
pickle.dump(d,f)

def filter(oldfile, newfile):
    file1=open("oldfile","r")
    file2=open("newfile","w")
    while True:
        text=file1.readline()
        if len(text)==0:
            continue
        file2.write(text)
    file1.close()
    file2.close()
    filter(sports.dat, atheletics.dat)'''



#WAP to store the following information in a Binary File in the form of a list of 3 elements: Name, Salary and DOB, also write the code to increase the salary by 2000 of employees whose name starts with a P

'''import pickle
f=open('Employee.dat','wb+')
n=[]
while True:
    Name=input("Enter name of employee")
    Salary=int(input("Enter salary of employee"))
    DOB=input("Enter date of birth")
    n.append([Name,Salary,DOB])
    c=input("Continue?")
    if c.lower()=='n':
        break
pickle.dump(n,f)
f.flush()
f.seek(0)
x=pickle.load(f)
for i in x:
    print(i)
    if i[0][0]=='p' or i[0][0]=='P':
        (i[1])+=2000
        print(x)'''


#WAF 'amcount' it should read each character of a text file and should display the occurence of the characters a and m in both capatle and small cases. In a CSV file

'''def amcount():
    f=open('count.dat','r')
    data=str(f.read())
    count=0
    for ch in data:
        if ch in"amAM":
            count=count+1
    print("No. of occurences : ", count)
    f.close()
amcount()'''

#WAP to read the following details of a sports performance in your school, in  tuple: Sport,competition and prizes won and store into a CSV file delimited by a tab. 

'''import csv
f=open("Sport.csv", "w+")
t=()
while True:
    sport=input("Enter name of the sport: ")
    competition=input("Enter name of competition: ")
    prizes=int(input("Enter number of prizes won: "))
    t=(sport,competition,prizes)
    c=input("Continue? ")
    if c.lower()=='n':
        break
    a=csv.writer(f,delimiter="\t")
    a.writerow(t)
f.close()'''

def add(Directory):
    a=eval(input("Enter the values"))
    Directory.append(a)
    print(Directory)
def delete(Directory):
    if len(Directory)==0:
        print('Underflow')
    else:
        Directory.pop()
        print(Directory)

Directory=[]
c=input("1 to add, 2. to delete, 3. for display")
if c=='1':
    add(Directory)
if c=='2':
    delete(Directory)
if c=='3':
    print(Directory)
    
