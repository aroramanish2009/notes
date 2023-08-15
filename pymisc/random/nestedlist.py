if __name__ == '__main__':
    all_students = []
    all_scores = []
    for _ in range(int(input())):
        each_student = []
        name = input()
        score = float(input())
        each_student.append(name)
        each_student.append(score)
        all_scores.append(score)
        all_students.append(each_student)
    sorted_all_students = sorted(all_students, key = lambda i: i[1])
    all_scores.sort()
    all_scores_set = set(all_scores)
    non_dup_all_scores = [i for i in all_scores_set]
    non_dup_all_scores.sort()
    if len(non_dup_all_scores) == 1:
        second_item_score = non_dup_all_scores[0]
    else:
        second_item_score = non_dup_all_scores[1]
    second_lowest_scorer = []
    for sorted_all_student in sorted_all_students:
        if sorted_all_student[1] == second_item_score:
            second_lowest_scorer.append(sorted_all_student[0])
    for i in sorted(second_lowest_scorer):
        print (i)
    
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
[['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39.0], ['Akriti', 41.0]]
'''
