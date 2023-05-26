file1 = open('crap.txt', 'r')
Lines = file1.readlines()
#['noop\n', 'addx 3\n', 'addx -5\n']

X = 1
count = 1
sumofsum = 0
for i in Lines: 
  if 'noop' in i:
    count += 1
  elif 'addx' in i:
    count += 2
    number = int(i.rsplit(' ', -1)[-1])
    X = X + number
  if count == 20:
    sig20 = X * 20 
    print ("20 cycle: " + str(sig20))
    sumofsum += sig20
  elif count == 60:
    sig60 = X * 60
    print ("60 cycle: " + str(sig60))
    sumofsum += sig60
  elif count == 100:
    sig100 = X * 100
    print ("100 cycle: " + str(sig100))
    sumofsum += sig100
  elif count == 140:
    sig140 = X * 140
    print ("140 cycle: " + str(sig140))
    sumofsum += sig140
  elif count == 180:
    sig180 = X * 180
    print ("180 cycle: " + str(sig180))
    sumofsum += sig180
  elif count == 220:
    sig220 = X * 220
    print ("220 cycle: " + str(sig220))
    sumofsum += sig220

print (sumofsum)
