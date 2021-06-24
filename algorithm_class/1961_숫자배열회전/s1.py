"""
# 회전은 어떤 방식으로 구현하면 쉬울까?
# 행렬을 돌릴려고 하기보다는 행과 열의 축을 돌리는게 더 빠를것 같은데
# 긍까 행렬만 돌리는게 아니라 종이 자체를 돌린다고 생각하자
# or 내 고개를 돌린다고 생각하자
"""
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]



    # 회전한것을 저장할 리스트
    rotate = [[] for _ in range(N)]

    # 90도 회전
    for j in range(N):
        ans = ''
        for i in range(N - 1, -1, -1):
            ans += str(matrix[i][j])
        rotate[j].append(ans)


    # 180도 회전
    for i in range(N-1, -1, -1):
        ans = ''
        for j in range(N-1, -1, -1):
            ans += str(matrix[i][j])
        rotate[N-1-i].append(ans)

    #270도 회전
    for j in range(N-1, -1, -1):
        ans = ''
        for i in range(N):
            ans += str(matrix[i][j])
        rotate[N-1-j].append(ans)

    # 출력
    print("#{}".format(tc))
    for i in range(N):
        print(*rotate[i])