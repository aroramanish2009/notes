happiness = 0
firstinput = input()
arry = [ i for i in input().split()]
seta = { j for j in input().split()}
setb = { k for k in input().split()}
for item in arry:
    if item in seta:
        happiness += 1
    if item in setb:
        happiness -= 1

print (happiness)
