def show_words():
    f = open('notes.txt','r')
    x = f.readlines()
    for i in x:
        a = i.split()
        if len(a) == 5:
            print(i)
    f.close()

show_words()