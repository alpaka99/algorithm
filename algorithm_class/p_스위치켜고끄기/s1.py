import sys
sys.stdin = open('input.txt', 'r')

# 남자일때의 switch 변형
def male(switch, num):
    # 받은 수의 배수에 해당하는 switch의 상태를 바꿈
    n = num
    while n < len(switch):
        # xor 연산으로 1은 0, 0은 1로 바뀜
        switch[n] = switch[n] ^ 1
        n += num


def female(switch, num):
    # 받은 수부터 좌우대칭이 가장 많은 스위치를 포함하는 구간의 스위치 상태를 바꿈
    # 좌우 대칭이 얼마나 긴지 어떻게 찾아볼까
    i = 1
    while num + i < len(switch) and 0 <= num - i:
            if switch[num - i] == switch[num + i]:
                i += 1
            else:
                i -= 1
                break
    # 어디까지가 대칭인지 구함. 그러면 그 범위만큼을 바꿈
    for j in range(num - i, num +i +1):
        switch[j] = switch[j] ^ 1

# 스위치 갯수
n = int(input())

# 각 스위치의 상태
# 앞에 -1을 더 더해줘야 배수부분에서 제대로 작동
switch = [-1] + list(map(int, input().split())) + [-1]

# 학생 수
N = int(input())
# 성별, 받은 수
for i in range(N):
    # 남자는 1, 여자는 2
    g, num = map(int, input().split())
    # g = 1 or 2,
    if g-1:
        female(switch, num)
    else:
        male(switch, num)
# 처음에 넣어놓은 0 제거
switch.pop(0)
switch.pop()
# 아니 출력 뭐야...
while len(switch) >= 20:
    print(*switch[:20])
    switch = switch[20:]
print(*switch)