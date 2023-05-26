with open("anothersample.txt", 'r') as file:
    #print (file.read().strip().split("\n\n"))
    for section in file.read().strip().split("\n\n"):
        print (section.split("\n"))

