import sys
sys.stdin = open('input.txt', 'r')


global max_money

def bfs(ad_list:list, S:int, money_list:list, cur_money:int, restaurant:list):
    # 현재 어느 위치인지와 어디와 연결되어있는지
    ad_nodes = ad_list[S]
    cur_money += money_list[S]
    money_list[S] = 0
    if ad_nodes == []:
        if S in restaurant:
            global max_money
            if cur_money > max_money:
                max_money = cur_money
    else:
        while ad_nodes:
            tmp = ad_nodes.pop()
            bfs(ad_list, tmp, money_list, cur_money, restaurant)





# N은 교차로의 수, M은 도로의 수
N, M = map(int, input().split())


# 인접 리스트 생성
ad_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ad_list[a].append(b)

# 각 교차점에 얼마있는지 저장되어있는 리스트
money_list = [0 for _ in range(N+1)]
for i in range(1,N+1):
    money_list[i] += int(input())

# S 출발장소 P 레스토랑 갯수
S, P = map(int, input().split())

# 레스토랑인 node
restaurant = list(map(int, input().split()))

# bfs돌리면서 다른곳으로 갈 수 없으면서 restaurant인 곳에서 최대가격 비교
# 재귀로 들어가면서 들어갈때 가격 더하고 나올때 가격 뺴야겠다

max_money = 0

