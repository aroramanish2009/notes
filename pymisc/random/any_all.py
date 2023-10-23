'''
You are given a space separated list of integers. If all the integers 
are positive, then you need to check if any integer is a palindromic 
integer.

Input:
5
12 9 61 5 14 
Output:
True


>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
'''

lenstr = input()
mylist = list(map(int,input().split(" ")))
if all(num > 0 for num in mylist):
    print (any(str(num) == str(num)[::-1] for num in mylist))
else:
    print (False)
