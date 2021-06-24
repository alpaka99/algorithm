import sys
sys.stdin = open('input.txt', 'r')

# 햄버거 재료 조합 구함
def powerset(ingredient_info, L):
    max_point = 0
    for i in range(1<<N):
        cur_combination = []
        for j in range(N):
            if (1<<j) & i:
                cur_combination.append(ingredient_info[j])
            # 해당 조합이 제한조건을 만족하는지 검사
        ans =  satisfy_limit(cur_combination, L)
        if max_point < ans:
            max_point = ans

    return max_point

# 제한조건 만족하는지 확인
def satisfy_limit(cur_combination, L):
    total_calories = 0
    total_point = 0
    for i in range(len(cur_combination)):
        total_calories += cur_combination[i][1]

    if total_calories <= L:
        for j in range(len(cur_combination)):
            total_point += cur_combination[j][0]

    return total_point

for tc in range(1, int(input())+1):
    # N: 재료의 수, L: 칼로리 제한
    N, L = map(int, input().split())

    # [맛 점수, 칼로리]
    ingredient_info = [list(map(int, input().split())) for _ in range(N)]

    
    # 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수
    print("#{} {}".format(tc,powerset(ingredient_info, L)))

