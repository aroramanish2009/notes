with open('sample.txt', 'r') as sample_file:
    sample_lines=sample_file.read().split("\n")
with open('main.txt', 'r') as file1:
    Lines=file1.read().split("\n")
#print (sample_lines)
#print (Lines)

def max_cal(sample_data):
    x = 0
    total_list = []
    for i in sample_data:
      if i:
          i = int(i)
          x = x + i
      else:
          x = int(x)
          total_list.append(x)
          x = 0
    return (total_list)
def main():
  print (max(max_cal(Lines)))
  part2 = max_cal(Lines)
  part2 = sorted([int(x) for x in part2])
  print (part2)
  print (int(part2[-1]) + int(part2[-2]) + int(part2[-3])) 

if __name__ == "__main__":
    main()
