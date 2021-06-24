import sys
sys.stdin = open('input.txt', 'r')

# N개의 식재료
# 각각 N/2개씩 나누어 두개의 요리 A, B를 만듬
# 맛의 차이가 최소가 되도록 재료를 배분
# 재료마다 시너지가 있음

def powerset(N:int, cnerge:list):
    if len(cnerge) == 2:
        powersets.append(cnerge[:])
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            cnerge.append(i)
            powerset(N,cnerge)
            cnerge.pop()
            visited[i] = 0

def powerset2(N:int, cnerge2:list):
    if len(cnerge2) == 2:
        powersets2.append(cnerge2[:])
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            cnerge2.append(i)
            powerset2(N, cnerge2)
            cnerge2.pop()
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 이 문제야말로 powerset 아닐까
    visited = [ 0 for _ in range(N)]

    powersets = []
    powersets2 = []

    powerset(N, [])


    print(powersets)
    powersets.reverse()
    print(powersets)
    