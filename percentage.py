if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_score = student_marks[query_name]
    score_sum = 0
    
    for num in student_score:
        score_sum += num

    avg = score_sum/3
    print('%.2f' % avg)    