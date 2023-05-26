file1 = open('crap.txt', 'r')
Lines = file1.read().splitlines() 

#['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']

C = len(Lines)
print (C)
M = max(Lines, key=len)
print (len(M))
L = 0
S_Loc = None
D_Loc = None
for line in Lines:
  P = 0
  for item in line:
    if item == 'S':
      S_Loc = str(L) + '-' + str(P)
    elif item == 'E':
      D_Loc = str(L) + '-' + str(P)
    P += 1
  L += 1

print (S_Loc)
print (D_Loc)
#20-0, 20-149
Steps = 0
while S_Loc != D_Loc:
  print (S_Loc.split('-')[0])
  
       
  Steps += 1  
  break
