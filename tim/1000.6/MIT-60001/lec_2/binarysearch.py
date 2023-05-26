import pdb
arry = [1,2,4,7,15,28,45,89]
target = 45


def binarysrh(arry,target):
    #pdb.set_trace()
    start = 0
    end = len(arry) - 1
    while start <= end:
        mid = (start + end) // 2
        if arry[mid] == target:
            return mid
        elif arry[mid] < target:
            start = mid + 1
        elif arry[mid] > target:
            end = mid - 1
    return -1

print (binarysrh(arry,target))
