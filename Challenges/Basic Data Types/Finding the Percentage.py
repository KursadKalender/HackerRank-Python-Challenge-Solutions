if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    values = student_marks[query_name]
    sum=0
    for i in range(len(values)):
        sum+=values[i]
    average=sum/len(values)
    print(f"{average:.2f}")
