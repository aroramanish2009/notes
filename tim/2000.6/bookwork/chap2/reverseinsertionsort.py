'''

Loop Invariant: Helps you reason about the correctness of a loop by ensuring that a certain condition remains true throughout the loop's execution. 
  - Initialization: This defines that the Loop Invariant is correct before you have started the iteration of the loop.
  - Maintenance: Loop Invariant remains correct after the complition of the specific iteration of the loop. 
  - Termination: Loop Invariant will be correct after the termination of the loop impling the correctness of your solution. 

Insertion Sort in reverse order aka smallest in the end
'''

myarray = [2,23,3,45,4,56,867,22,3]

for i in range(1,len(myarray)):
    key = myarray[i]
    j = i - 1
    while j >= 0 and myarray[j] < key:
        myarray[j + 1] = myarray[j]
        j = j - 1
    myarray[j + 1] = key

print (myarray)
