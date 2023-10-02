from collections import OrderedDict
myordict = OrderedDict()
for i in range(int(input())):
    mystr = str(input())
    key,value = str(' '.join(mystr.split(' ')[:-1])), int(''.join(mystr.split(' ')[-1]))
    if key not in myordict:
        myordict[key] = value
    else:
        value = value + myordict[key]
        myordict[key] = value

for k,v in myordict.items():
    print (k,v)
