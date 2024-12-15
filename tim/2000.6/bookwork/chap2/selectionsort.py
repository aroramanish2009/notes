'''

Loop Invariant: Helps you reason about the correctness of a loop by ensuring that a certain condition remains true throughout the loop's execution. 
  - Initialization: This defines that the Loop Invariant is correct before you have started the iteration of the loop.
  - Maintenance: Loop Invariant remains correct after the complition of the specific iteration of the loop. 
  - Termination: Loop Invariant will be correct after the termination of the loop impling the correctness of your solution. 

Selection sort:
Loop Invariant: At each loop, myarray[0:startpt] is sorted. 
Initialization: At start, the single element in the list is sorted. 
Maintenance: At every external loop iteration, myarray[0:startpt] stays sorted. 
Termination: List is sorted when external loop finishes at N. 
Theta for selection sort: N^2 
Theta for selection sort for best case: N^2 
Theta for selection sort for worst case: N^2
'''

myarray = [2,23,3,45,4,56,867,22,3]

startpt = 0

while startpt != len(myarray):
    for item in range(len(myarray)):
        if myarray[startpt] < myarray[item]:
            myarray[startpt],myarray[item] = myarray[item],myarray[startpt]
    startpt +=1

print (myarray)
