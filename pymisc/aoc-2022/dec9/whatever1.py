file1 = open('crap1.txt', 'r')
data = file1.readlines()

def f(x, k):
	return "#" if abs(x-(k%40))<=1 else "."

def solve():
  x=1
  a=[]
  g=[]
  for l in data:
    tokens = l.split()
    if tokens[0]=="noop":
      a.append(x)
      g.append(f(x, len(g)))
    else:
      a.append(x)
      a.append(x)
      g.append(f(x, len(g)))
      g.append(f(x, len(g)))
      x += int(tokens[1])
  ans=0
  for i in [20, 60, 100, 140, 180, 220]:
    ans+=a[i-1]*i
  print(ans)
  for i in range(0, 201, 40):
    print("".join(g[i:i+40]))

solve()
