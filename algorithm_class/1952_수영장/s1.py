
# 가장 적은 비용으로 수영장 이용
# 1달 이용권: 매달 1일 시작
# 3달 이용권: 매달 1일 시작, 매년 말에는 남아있어도 그 다음해에 사용 불가
# 1년 이용권: 매년 1월 1일

import sys
sys.stdin = open('input.txt', 'r')

global lowest


def dp(plan:list):
    # 재귀 탈출 조건
    if len(plan) == 0:
        return 0
    
    
    # 아직 12월까지 연산을 다 하지 않았으면 연산
    # 연산 방법은 4가지 -> 각각에 대해서 dp를 해서 나눠나가나?
    cost_list = [0 for _ in range(4)] # 각 연산 방법들의 가격을 저장하는 리스트

    # 1. 가장 앞 달을 1일권으로 계산
    new_plan = plan[1:]
    num1 = price[0]
    num2 = plan[0]
    cost_list[0] = num1*num2+dp(new_plan)

    # 2. 가장 앞 1달을 1달권으로 계산
    cost_list[1] = price[1]+dp(new_plan)

    # 3. 가장 앞 3달을 3달권으로 계산
    new_plan = plan[3:]
    cost_list[2] = price[2] + dp(new_plan)

    # 4. 남은 기간 전부를 1년권으로
    cost_list[3] = price[3]

    return min(cost_list)


for tc in range(1, int(input())+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split())) # 연간 이용 계획
    #print(price, plan)
    plan_cpy = plan[:]

    print("#{} {}".format(tc, dp(plan)))
