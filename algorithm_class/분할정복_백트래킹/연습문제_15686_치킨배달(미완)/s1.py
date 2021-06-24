import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # N, M
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 치킨거리 = 가장 가까운 치킨집과의 거리
    # 맨해튼 거리를 사용
    # 0은 빈 칸, 1은 집, 2는 치킨집

    # M개의 치킨집을 폐업
    # 도시의 치킨거리가 가장 작게

    # 그러면 전체 치킨집 중 M개를 삭제시키고 치킨거리를 구하는 방식으로..?

    # 0. 전체 치킨집들 구하기
    chicken_shop = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                chicken_shop.append([i,j])
    
    # 1. M개의 치킨집 구하기
