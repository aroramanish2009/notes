if __name__ == '__main__':
    mylist = []
    commands = []
    N = int(input())
    for i in range(N):
        command = (input())
        commands.append(command)
    for command in commands:
        if command.split()[0] == "append":
            mylist.append(int(command.split()[1]))
        elif command.split()[0] == "print":
            print (mylist)
        elif command.split()[0] == "remove":
            mylist.remove(int(command.split()[1]))
        elif command.split()[0] == "sort":
            mylist.sort()
        elif command.split()[0] == "pop":
            mylist.pop()
        elif command.split()[0] == "reverse":
            mylist.reverse()
        elif command.split()[0] == "insert":
            mylist.insert(int(command.split()[1]), int(command.split()[2]))
