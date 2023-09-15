listoftup = []
for i in range(int(input())):
    mystr = input()
    listoftup.append((mystr.split()[0],mystr.split()[1]))
for item in listoftup:
    try:
        print (int(item[0]) // int(item[1]))
    except Exception as e:
        print ("Error Code:", e)
