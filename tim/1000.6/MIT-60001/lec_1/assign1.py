import sys, math
from colorama import Fore, Back, Style

print (Fore.BLUE,"Enter number x: ", sys.argv[1])
print (Fore.BLUE,"Enter number y: ", sys.argv[2])
x = int(sys.argv[1])
y = int(sys.argv[2])
print (Fore.BLUE, "X**y = ", Fore.WHITE, x**y )
print (Fore.BLUE,"log(x) =", math.log(x, 2))
print (Style.RESET_ALL)
