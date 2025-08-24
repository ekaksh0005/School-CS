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
    
