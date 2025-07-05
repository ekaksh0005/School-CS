def palindrome(x):
    i=''
    for j in x:
        if j.isalpha()==True:
            i+=j
    if i==i[::-1]:
        print("It is a Palindrome")
    else:
        print("It is NOT a Palindrome")
s=input("Enter a Input: ")
palindrome(s)
