import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, int(input())+1):


    tc = int(input())

    # 학생수는 1000명 점수는 0점이상 100점 이하
    students = list(map(int, input().split()))

    # 학생 점수를 저장할 count 리스트
    count = [0]*101 # 100까지 인덱스 접근 하고 싶어서

    for i in range(len(students)):
        count[students[i]] += 1

    max_value, max_idx = 0, 0
    for i in range(len(count)):
        if count[i] >= max_value:
            max_value = count[i]
            max_idx = i

    print("#{} {}".format(tc, max_idx))