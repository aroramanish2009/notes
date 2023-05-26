import sys, re
import pdb
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    part1, part2 = sample_file.read().split("\n\n")
    len_crt = len(part1.splitlines())
    list_part1 = []
    for i in range(len_crt - 1):
        string = re.sub(r'\s\s\s\s', '[X] ', part1.splitlines()[i])
        list_part1.append(string.split())
    clean_big_list = []
    for ip1 in list_part1:
        clean_small_list = []
        for i in ip1:
            if '][' in i:
                ilen = len(i) // 2
                item1 = i[:ilen]
                item2 = i[ilen:]
                clean_small_list.append(item1)
                clean_small_list.append(item2)
            else:
                clean_small_list.append(i)
        clean_big_list.append(clean_small_list)
    stack_list = part1.splitlines()[-1].split()
    stack_dict = {key: [item[index] for item in clean_big_list if '[X]' not in item[index]]  for index, key in enumerate(stack_list)}
    instruct_list = [i for i in part2.splitlines() if i]
        
def task_1(stack_dict, instruct_list):
    for i in instruct_list:
        move_items = int(i.split()[1])
        move_from_key = i.split()[3]
        move_to_key = i.split()[-1]
        for i in range(move_items):
            move_elements = stack_dict[move_from_key][:1]
            print (move_elements)
            print (stack_dict[move_from_key])
            stack_dict[move_from_key] = stack_dict[move_from_key][1:]
            print (stack_dict[move_from_key])
            stack_dict[move_to_key].insert(0, move_elements)
        print (stack_dict)

def task_2(stack_dict, instruct_list):
    for i in instruct_list:
        move_items = int(i.split()[1])
        move_from_key = i.split()[3]
        move_to_key = i.split()[-1]
        move_elements = stack_dict[move_from_key][:move_items]
        print (move_elements)
        print (stack_dict[move_from_key])
        stack_dict[move_from_key] = stack_dict[move_from_key][move_items:]
        print (stack_dict[move_to_key])
        stack_dict[move_to_key] = move_elements + stack_dict[move_to_key]
        print (stack_dict[move_to_key])
    print (stack_dict)
        
def main():
    task_2(stack_dict, instruct_list)

if __name__ == "__main__":
    main()
