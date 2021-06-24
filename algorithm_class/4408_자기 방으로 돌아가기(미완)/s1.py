import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(students):
    if len(students) <= 1:
        return students
    pivot = []
    pivot.append(students[0])

    left = []
    right = []
    for i in range(1, len(students)):
        if students[i][0] < pivot[0][0]:
            left.append(students[i])
        elif students[i][0] > pivot[0][0]:
            right.append(students[i])
        else:
            pivot.append(students[i])

    return quick_sort(left) + pivot + quick_sort(right)

for tc in range(1, int(input())+1):
    # 돌아가야할 학생 수
    N = int(input())

    # 단위시간
    time = 1

    students = []
    for i in range(N):
        start, goal = map(int, input().split())
        students.append([start, goal])

    # 시작점에 대해서 sorting 한번 해야 쫙 나올거 같은데
    # quick sort
    sorted = quick_sort(students)
    sorted = students
    cur_student = sorted.pop()

    while sorted:
        nxt_student = sorted.pop()
        # 시간이 걸리는 case 1. 뒤에 있는 학생의 도착점이 앞에 있는 학생의 도착점보다 낮음
        if cur_student[1] < nxt_student[1]:
            time += 1
            cur_student = nxt_student
            continue
        # case 2. 뒤에 있는 학생의 출발점이 앞에 학생의 도착점과 동일선상이거나 그 밑
        if cur_student[0] <= nxt_student[1]-1:
            time += 1
            cur_student = nxt_student
            continue
        if cur_student[0] == nxt_student[1]:
            time += 1
            cur_student = nxt_student
            continue
        cur_student = nxt_student
        # case 3. 홀->홀 , 짝->짝 인 경우에서 근데 이건 2에서 걸리지 않냐



    print("#{} {}".format(tc,time))
