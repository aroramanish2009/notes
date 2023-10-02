'''
Input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Output:
1 2
'''
from collections import deque
d = deque()
for i in range(int(input())):
    mylist = []
    usercommand = str(input())
    mylist = usercommand.split(' ')
    if len(mylist) > 1:
        action = str(mylist[0])
        value = int(mylist[1])
        if action == "append":
            d.append(value)
        elif action == "appendleft":
            d.appendleft(value)
    else:
        action = mylist[0]
        if action == "pop":
            d.pop()
        elif action == "popleft":
            d.popleft()
for i in d:
  print (i, end=" ")
