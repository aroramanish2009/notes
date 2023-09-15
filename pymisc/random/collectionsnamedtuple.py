#from collections import namedtuple
#Student = namedtuple('Student', 'ID	MARKS	NAME	CLASS')
numstudent = int(input())
marks_index = str(input()).split().index("MARKS")
marks = 0
for i in range(numstudent):
        marks += int(str(input()).split()[marks_index])
print (f"{(marks / numstudent):.2f}")
      
    
'''
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
'''    
