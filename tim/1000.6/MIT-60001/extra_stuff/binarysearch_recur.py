'''
Make sure to return from one recursion to other, if you do 
not return values then you end up with None
'''

arry = [1,2,4,7,15,28,45,89]
target = 45
startlist = 0
lengthlist = len(arry)
endlist = lengthlist - 1

def binary_recur(arry,target,startlist,endlist):
    if startlist <= endlist:
        midlist = (startlist + endlist) // 2
        if arry[midlist] == target:
            return midlist
        elif arry[midlist] < target:
            return binary_recur(arry,target,midlist + 1,endlist)
        else:
            return binary_recur(arry,target,startlist,midlist - 1)
    else:
        return -1 

location = binary_recur(arry,target,startlist,endlist)
if location:
    print ("Found Target:", arry[location], "at Index:", location, "of Array", arry)
else:
    print ("Target not found")
