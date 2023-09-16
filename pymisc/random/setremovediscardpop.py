'''
set.remove(x) - remove element from set, keyerror if element not in set
set.discard(x) - remove element from set, NO keyerror if element not in set
set.pop() - remove arbitrary element from set, keyerror if set is empty.
'''
lenset = int(input())
myset = set([int(i) for i in input().split() ])
for i in range(int(input())):
    command = input()
    if "pop" in command and myset:
        myset.pop()
    elif "remove" in command:
        item = int(command.split()[1])
        if item in myset:
            myset.remove(item)
    elif "discard" in command:
        item = int(command.split()[1])
        myset.discard(item)

print (sum(myset))
