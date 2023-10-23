'''
Input:
3
1 2
3 4
10 6

output
5 8

basically takes a list of fractions, applies product lambda on list 2 items at a time

'''


from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y: x *y, fracs) # basically applies the function in firs arg to 2 elements in list until list is completed.
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):  # _ is throw away variable 
        fracs.append(Fraction(*map(int, input().split()))) # * unpacks to a function, map applies function in first arg to each value in next arg
    result = product(fracs)
    print(*result)  # * again is unpacking for print function
