import string
with open('sample.txt', 'r') as sample_file:
    sample_lines=sample_file.read().split("\n")
with open('main.txt', 'r') as file1:
    Lines=file1.read().split("\n")
print (sample_lines)
#print (Lines)

lower_al_list = list(string.ascii_lowercase)
upper_al_list = list(string.ascii_uppercase)

#print (int(lower_al_list.index("c")) + 1)

def find_sum(datalist):
    total = 0 
    for i in datalist:
        compart_1, compart_2 = i[:len(i)//2], i[len(i)//2:]
        common = ''.join(set(compart_1).intersection(compart_2))
        if common.islower():
            total = total + int(lower_al_list.index(common)) + 1
        elif common.isupper():
            total = total + int(upper_al_list.index(common)) + 27
    return(total)
        
def priority_sum(datalist):
    newtotal = 0
    subset = []
    for i in datalist:
        subset.append(i)
        if len(subset) == 3:
            item_1, item_2, item_3 = subset[0], subset[1], subset[2]
            common_1 = ''.join(set(item_1).intersection(item_2))
            common = ''.join(set(item_3).intersection(common_1))
            if common.islower():
                newtotal = newtotal + int(lower_al_list.index(common)) + 1
            elif common.isupper():
                newtotal = newtotal + int(upper_al_list.index(common)) + 27
            subset = []       
    return(newtotal)

def main():
    print (find_sum(Lines))
    print (priority_sum(Lines))

if __name__ == "__main__":
    main()
