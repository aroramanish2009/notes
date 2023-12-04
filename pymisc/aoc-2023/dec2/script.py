import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

total = 0
board = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']
gear_nums = defaultdict(list)

#for line in open('sample1.txt').readlines():
  #board.append( line.strip() )

'''

['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']
finditer
<re.Match object; span=(0, 3), match='467'> 0 3 467
<re.Match object; span=(5, 8), match='114'> 5 8 114
<re.Match object; span=(2, 4), match='35'> 2 4 35
<re.Match object; span=(6, 9), match='633'> 6 9 633
<re.Match object; span=(0, 3), match='617'> 0 3 617
<re.Match object; span=(7, 9), match='58'> 7 9 58
<re.Match object; span=(2, 5), match='592'> 2 5 592
<re.Match object; span=(6, 9), match='755'> 6 9 755
<re.Match object; span=(1, 4), match='664'> 1 4 664
<re.Match object; span=(5, 8), match='598'> 5 8 598
'''

num_pattern = re.compile('\d+')

def data_mass1(start_y, start_x, end_y, end_x, num):
  global gear_nums
  for y in range(start_y, end_y+1):
    for x in range(start_x, end_x+1):
      if y >= 0 and y < len(board) and x >= 0 and x < len(board[y]):
        if board[y][x] not in '0123456789.':
          if board[y][x] == '*':
            gear_nums[ (y,x) ].append(num)
          return True
  return False

for row_num in range(len(board)):
  for match in re.finditer(num_pattern, board[row_num]):
    print (match,match.start(),match.end(),match.group(0))
    if data_mass1(row_num-1, match.start()-1, row_num+1, match.end(), int(match.group(0))):
      total += int(match.group(0))

print("Part 1")
print (total)

rat_total = 0
for k,v in gear_nums.items():
  if len(v) == 2:
    rat_total += v[0] * v[1]
print("Part 2")
print (rat_total)
