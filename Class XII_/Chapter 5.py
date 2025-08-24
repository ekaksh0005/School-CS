'''s=[]
def push(s):
    x=int(input("Enter no. : "))
    s.append(x)

def pop(s):
    if len(s)==0:
        print("Underflow!")
    else:
        s.pop(x)
while True:
    c=int(input("Enter a choice : "))
    if c==1:
        push(s)
    elif c==2:
        pop(s)
    elif c==3:
        print(s)

    ch=int(input("Do you wish to continue?"))
    if ch=='n':
        break '''
    
#10 Write add(Directory) and delete(Directory) methods to add and remove contacts using appen and pop operations in Stack. 

'''Directory=[]
def add(Directory):
    a=eval(input("Enter the values"))
    Directory.append(a)
def delete(Directory):
    if len(Directory)==0:
        print('Underflow')
    else:
        Directory.pop()
       
while True:

    c=input("1 to add, 2. to delete, 3. for display")
    if c=='1':
        add(Directory)
    if c=='2':
        delete(Directory)
    if c=='3':
        print(Directory)'''

#15 WAP to create a Stack for storing only odd numbers out of all the numbers entered by the user . Display the content of the stack along with the largest odd number in the stack. 
def add(a):
    Stack.append(a)
Stack=[]
while True:
    a=eval(input("Enter number to enter"))
    if a%2!=0:
        add(a)
        c=input("Continue?")
        if c.lower=='n':
            break
    else:
        c=input("Continue?")
        if c.lower()=='n':

            break
    print(Stack)
x=Stack.pop()
for i in Stack:
    if Stack.pop()>x:
        Max=i
    else:
        Max=x
print('Maximum number is :',Max)
