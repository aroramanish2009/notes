'''
input: 100,000,000.000
output:
100
000
000
000
'''
import re
print("\n".join(re.split(r"\,|\.", input())))
