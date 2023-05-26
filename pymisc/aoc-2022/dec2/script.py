with open('sample.txt', 'r') as sample_file:
    sample_lines=sample_file.read().split("\n")
with open('main.txt', 'r') as file1:
    Lines=file1.read().split("\n")
#print (sample_lines)
#print (Lines)

A = 1
B = 2
C = 3
X = 1
Y = 2
Z = 3

def cal_score(elf_list):
    score = 0
    for i in elf_list:
        if i:
            if (i[0]) == 'A' and (i[-1]) == 'X':
                score = score + 4
            elif (i[0]) == 'B' and (i[-1]) == 'Y':
                score = score + 5
            elif (i[0]) == 'C' and (i[-1]) == 'Z':
                score = score + 6
            elif (i[0]) == 'A' and (i[-1]) == 'Y':
                score = score + 8
            elif (i[0]) == 'A' and (i[-1]) == 'Z':
                 score = score + 3
            elif (i[0]) == 'B' and (i[-1]) == 'X':
                 score = score + 1
            elif (i[0]) == 'B' and (i[-1]) == 'Z':
                 score = score + 9
            elif (i[0]) == 'C' and (i[-1]) == 'X':
                 score = score + 7
            elif (i[0]) == 'C' and (i[-1]) == 'Y':
                 score = score + 2
    print (score)

def cal_score_2(elf_list):
    score2 = 0
    for i in elf_list:
        if i:
            if (i[0]) == 'A' and (i[-1]) == 'X':
                score2 = score2 + 3
            elif (i[0]) == 'B' and (i[-1]) == 'Y':
                score2 = score2 + 5
            elif (i[0]) == 'C' and (i[-1]) == 'Z':
                score2 = score2 + 7
            elif (i[0]) == 'A' and (i[-1]) == 'Y':
                score2 = score2 + 4
            elif (i[0]) == 'A' and (i[-1]) == 'Z':
                 score2 = score2 + 8
            elif (i[0]) == 'B' and (i[-1]) == 'X':
                 score2 = score2 + 1
            elif (i[0]) == 'B' and (i[-1]) == 'Z':
                 score2 = score2 + 9
            elif (i[0]) == 'C' and (i[-1]) == 'X':
                 score2 = score2 + 2
            elif (i[0]) == 'C' and (i[-1]) == 'Y':
                 score2 = score2 + 6
    print (score2)

def main():
    cal_score(Lines)
    cal_score_2(sample_lines)
    cal_score_2(Lines)

if __name__ == "__main__":
    main()
