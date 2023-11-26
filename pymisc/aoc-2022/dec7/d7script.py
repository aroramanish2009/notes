'''
Copied Code from reddit
'''
from collections import defaultdict

with open("sample.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []
for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        #Ignore these and move to next item in list
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            #Empty the stack if you see ..
            stack.pop()
        else:
            #If stack has anything in it and you got cd xx then create subdict. If stack is empty then create path with new dest
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        #for the path in stack .. add files size to sizes dict
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2
