'''
There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if is on top of then

sidelength[j] >= sidelength[i]

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

Result: No

After choosing the rightmost element,
, choose the leftmost element, . After than, the choices are and . These are both larger than the top block of size

Input Format

The first line contains a single integer
, the number of test cases.
For each test case, there are lines.
The first line of each test case contains , the number of cubes.
The second line contains space separated integers, denoting the sideLengths of each cube in that order. 

Result: Yes
Input:
    2
    6
    4 3 2 1 3 4
    3
    1 3 2
Output:
    Yes
    No

NOTE: Recursion fails on large data sets, possibly requires memoization 
NOTE: Sample code without deque
t=int(input())
for i in range(0,t):
    n=int(input())
    b=input()
    l=list(map(int,b.split()))[:n]
    count=0
    for x in range(0,int(n/2)):
        big1=max(l[x],l[n-1-x])
        big2=max(l[x+1],l[n-2-x])
        if(big1<big2):
            print('No')
            count=1
            break                
    if(count==0):
        print('Yes')
'''
from collections import deque

def canwepile(dcubelist,topcube):
    if len(dcubelist) == 1 and dcubelist[0] <= topcube:
        return ("Yes")
    elif len(dcubelist) == 1 and dcubelist[0] > topcube:
        return ("No")
    if dcubelist[0] == dcubelist[-1] and dcubelist[0] <= topcube:
        topcube = dcubelist[0]
        dcubelist.popleft()
        dcubelist.pop()
        return canwepile(dcubelist,topcube)
    elif dcubelist[0] <= topcube:
        topcube = dcubelist[0]
        dcubelist.popleft()
        return canwepile(dcubelist,topcube)
    elif dcubelist[-1] <= topcube:
        topcube = dcubelist[-1]
        dcubelist.pop()
        return canwepile(dcubelist,topcube)
    else:
        return ("No")
        
        
def main():
    for i in range(int(input())):
        lenofcubelist = int(input())
        cubelist = input().split(' ')
        cubelist = [int(i) for i in cubelist]
        if lenofcubelist == 1 or lenofcubelist == 2:
            print ("Yes")
            break
        dcubelist = deque(cubelist)
        if dcubelist[0] >= dcubelist[-1]:
            topcube = dcubelist[-1]
        else:
            topcube = dcubelist[0]
        dcubelist.pop()
        dcubelist.popleft()
        print (canwepile(dcubelist,topcube))


if __name__ == '__main__':
    main()
