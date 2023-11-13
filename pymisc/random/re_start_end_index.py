'''
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
[(m.start(), m.end() + 0) for m in re.finditer(r"(?=(i))", "vineetdoshi")]
'''
import re
mystr = input()
pat = input()
tup = [(m.start(), m.end() + (len(pat) - 1)) for m in re.finditer(r"(?=({}))".format(pat), mystr)]
if tup:
    print (*tup, sep='\n')
else:
    print (-1,-1)
