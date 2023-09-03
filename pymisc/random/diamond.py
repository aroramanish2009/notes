thickness = int(input())
if thickness % 2 == 0:
    thickness = thickness + 1

c = '*'


'''
# The width(10) included the item(&&) in total print.
#print ('&&'.rjust(10,'-')) 
#print ('&&'.center(10,'-'))
#print ('&&'.ljust(10,'-'))

Result
--------&&
----&&----
&&--------

'''

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness):
    #print ((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)) 
    print(((c*(thickness-i-1)).rjust(thickness-1)+c+(c*(thickness-i-1)).ljust(thickness)))
