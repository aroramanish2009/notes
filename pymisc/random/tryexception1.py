import re
regexlist = []
for i in range(int(input())):
    regexlist.append(input())
for item in regexlist:
    try:
        patt = 'r"' + item + '"'
        re.compile(patt)
        is_valid = True
    except re.error:
        is_valid = False
    print (is_valid)
