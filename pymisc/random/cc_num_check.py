'''
Valid: 
4253625879615786
4424424424442444
5122-2368-7954-3214
not-valid
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
'''
import re

for _ in range(int(input())):
    if re.search(r"(?!.*(\d)(?:-?\1){3})^[4|5|6]\d{3}(?:-?\d{4}){3}$",input()):
        print ("Valid")
    else:
        print ("Invalid")
