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
