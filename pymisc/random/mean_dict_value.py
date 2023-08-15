if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    num_score, sum_score = 0,0
    for i in student_marks[query_name]:
        num_score += 1
        sum_score = sum_score + i

    print (format(sum_score/num_score, ".2f"))
