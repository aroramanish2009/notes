'''

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.


'''
import re
mylist = list(input())

vendigits = []
dddigits = []
ppercase = []
owercase = []

for i in mylist:
    if i.isupper():
        ppercase.append(i)
    elif i.islower():
        owercase.append(i)
    elif i.isdigit():
        if re.search(r"[13579]",i):
            dddigits.append(i)
        else:
            vendigits.append(i)

finale = sorted(owercase) + sorted(ppercase) + sorted(dddigits) + sorted(vendigits)
print (''.join(finale))
