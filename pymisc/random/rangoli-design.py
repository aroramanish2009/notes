
'''
# The width(10) included the item(&&) in total print.
#print ('&&'.rjust(10,'-')) 
#print ('&&'.center(10,'-'))
#print ('&&'.ljust(10,'-'))

Result
--------&&
----&&----
&&--------



height = int(input("Enter odd num: "))
if height % 2 == 0:
    height = height + 1
width = 3 * height
c = '.|.'
top = height // 2
for i in range(top):
    print((c*i).rjust((width // 2) - 1,'-')+c+(c*i).ljust((width // 2) - 1,'-'))
print ("WELCOME".center(width,'-'))
for i in range(top):
    print ((c*(top - 1 - i)).rjust((width // 2) - 1, '-')+c+(c*(top - 1 - i)).ljust((width // 2) - 1, '-'))


input = 17
------------------------.|.------------------------
---------------------.|..|..|.---------------------
------------------.|..|..|..|..|.------------------
---------------.|..|..|..|..|..|..|.---------------
------------.|..|..|..|..|..|..|..|..|.------------
---------.|..|..|..|..|..|..|..|..|..|..|.---------
------.|..|..|..|..|..|..|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|..|..|..|..|..|..|.---
----------------------WELCOME----------------------
---.|..|..|..|..|..|..|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|..|..|..|..|..|..|.------
---------.|..|..|..|..|..|..|..|..|..|..|.---------
------------.|..|..|..|..|..|..|..|..|.------------
---------------.|..|..|..|..|..|..|.---------------
------------------.|..|..|..|..|.------------------
---------------------.|..|..|.---------------------
------------------------.|.------------------------
'''

import string

n = int(input())

def print_rangoli(num):
    mywordslist = list(string.ascii_lowercase[:num])
    reversemywordslist = mywordslist.copy()
    reversemywordslist.reverse()
    print (mywordslist, reversemywordslist)
    botcone = (2 * num) - 1
    widthcone = ((2 * num) - 1) + ((2 * num) - 2)
    print (botcone, widthcone)
    for i in range(num):
        if i == 0:
            print (("-".join(reversemywordslist[:i + 1]).rjust((widthcone // 2) + 1,'-')) + (("-".join(mywordslist) * i).ljust((widthcone // 2),'-')))
        else:
            print (("-".join(reversemywordslist[:i + 1]).rjust((widthcone // 2) + 1,'-')) + '-' + ("-".join(mywordslist[-i:]).ljust((widthcone // 2) - 1,'-')))
    for i in range(botcone  // 2):
        print (("-".join(reversemywordslist[:-i - 1]).rjust((widthcone // 2) + 1,'-')) + '-' + ("-".join(mywordslist[i + 2:]).ljust((widthcone // 2) - 1,'-')))

print_rangoli(n)
