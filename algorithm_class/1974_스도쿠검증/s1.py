import sys
sys.stdin = open('input.txt', 'r')

def garo(matrix):
    for i in range(9):
        # 숫자들이 1~9니까 10칸 만들고 마지막에 맨앞을 pop하자
        count = [0]*10
        for j in range(9):
            # 가로 한줄 숫자들을 채워넣고
            count[matrix[i][j]] += 1
        # 다 채워넣었을때 곂치는 것이나 없는게 있으면 스도쿠가 아님
        count.pop(0)
        if 0 in count or 2 in count:
            return False
    # 다 통과하면 True
    return True

def cero(matrix):
    for i in range(9):
        # 숫자들이 1~9니까 10칸 만들고 마지막에 맨앞을 pop하자
        count = [0]*10
        for j in range(9):
            # 가로 한줄 숫자들을 채워넣고
            count[matrix[j][i]] += 1
        # 다 채워넣었을때 곂치는 것이나 없는게 있으면 스도쿠가 아님
        count.pop(0)
        if 0 in count or 2 in count:
            return False
    # 다 통과하면 True
    return True

def cube(matrix):
    # 델타 써볼까?
    # 시계 방향으로 중, 북, 북동, 동, 남동, 남, 남서, 서, 북서
    dx = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

    # 시작 좌표
    # cube 0 의 중앙좌표
    x = 1

    
    # while문으로 9개의 큐브 확인
    while x < 9:
        y = 1
        while y < 9:
            count = [0]*10
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                count[matrix[nx][ny]] += 1
            count.pop(0)
            if 0 in count or 2 in count:
                return 0
            y += 3
        x += 3
    return 1

for tc in range(1, int(input())+1):
    # 9 by 9 matrix

    matrix = [list(map(int,input().split())) for _ in range(9)]

    # 어떻게 하면 예쁘게 풀 수 있을까
    # 간단하기는 함수를 나눠서 하나하나 비교하는게 제일 생각에는 간단한데
    ans = 0
    
    # 가로 검사
    ans = ans | garo(matrix)
    if not(ans):
        print("#{} {}".format(tc, ans))
        continue

    # 세로검사
    ans = ans & cero(matrix)
    if not (ans):
        print("#{} {}".format(tc, ans))
        continue
    
    # 마지막 cube검사
    ans = ans & cube(matrix)
    print("#{} {}".format(tc, ans))