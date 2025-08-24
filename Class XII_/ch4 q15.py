a=0
b=0
file=open('Poem.txt','r')
lst=file.readlines()
for i in lst:
    word= i.split()
    for j in word:
        if j=='To' or j=='to':
            a+=1
        elif j=='The' or j=='the':
            b+=1
print("Number of to:",a)
print("Number of the:",b)
file.close()
