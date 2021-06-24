import sys
from itertools import permutations
from collections import deque
sys.stdin = open('input.txt','r')

max_score = 0

def one_ining(order:list, ining:int, score:int, start_player:int):
    if ining == end_ining:
        global max_score
        max_score = max(max_score, score)
        return

    # 이 이닝에 선수들이 칠 확률
    # cur_rate = hits[ining]

    out = 0
    ining_score = 0
    batter_num = start_player
    base = deque()
    for _ in range(3):
        base.append(0)

    while out < 3:
        # case = cur_rate[order[batter_num]]
        case = hits[ining[order[batter_num]]]
        # 아웃
        if case == 0:
            out += 1
        # 홈런
        elif case == 4:
            while base:
                ining_score += base.popleft()
            ining_score += 1
            for _ in range(3):
                base.append(0)
        # 루타
        else:
            while case > 0:
                ining_score += base.popleft()
                if case == 1:
                    base.append(1)
                else:
                    base.append(0)
                case -= 1
        batter_num = (batter_num + 1) % 9
    one_ining(order, ining + 1, score + ining_score, batter_num)





# 안타 1, 2루타 2, 3루타 3, 홈런 4, 아웃 0
end_ining = int(input())

# 각 이닝당 선수의 타율
hits = [list(map(int, input().split())) for _ in range(end_ining)]



# 1번은 4번타자로 고정
player = [i for i in range(1, 9)]

perms = list(permutations(player))

# 각 타순에 몇번 선수인지
orders = []
for perm in perms:
    order = perm[:3] + [0] + perm[3:]
    one_ining(order, 0, 0, 0)


print(max_score)




