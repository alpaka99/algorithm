import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


# 벨트 회전하고 내릴 로봇 내림
def func1():
    # 내릴 로봇 내리고
    if dq[N-1][1]:
        dq[N-1][1] = False

    #회전
    tmp = dq.pop()
    dq.appendleft(tmp)


# 가장 먼저 올라간 로봇부터
# 다음칸에 로봇이 없고, 칸 내구도가 1 이상이고, 내리는 위치가 아니면
# 로봇 이동 및 내구도 1 감소
def func2():
    # 내리는 위치가 아니고
    dq[N-1][1] = False
    for i in range(N-2,-1,-1):
        # 어떤 칸에 로봇이 있을떄
        if dq[i][1]:
            # 다음칸에 로봇이 없고 내구도 1이상
                if dq[i+1][1] == False and dq[i+1][0]:
                    # 로봇 이동
                    dq[i][1] = False
                    dq[i+1][1] = True
                    dq[i+1][0] -= 1


# 올리는 칸의 내구도가 0 이상이고 로봇이 없으면 올림
# 로봇을 올리면 내구도 -1
def func3():
    if dq[0][0]:
        dq[0][1] = True
        dq[0][0] -= 1

# 전체 칸들의 내구도 조사
def func4():
    zero_cnt = 0
    for i in range(len(dq)):
        if dq[i][0] == 0:
            zero_cnt += 1

    if zero_cnt >= K:
        return 0
    else:
        return 1

# N은 벨트 반쪽의 길이, K는 내구도가 0인 칸의 제한 갯수
N, K = map(int, input().split())

input_data = list(map(int, input().split()))
belt = [[input_data[i],False] for i in range(N*2)]

dq = deque(belt)

key = 1
cnt = 0
while key:
    cnt += 1
    func1()
    func2()
    func3()
    key = func4()
    # print(cnt,dq)

print(cnt)


