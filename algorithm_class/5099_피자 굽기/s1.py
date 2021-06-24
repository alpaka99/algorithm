import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # N개의 피자를 넣는 화덕 M개의 피자
    N, M = map(int, input().split())

    pizza = list(map(int, input().split()))
    pizza_line = [] # 피자 줄 세우기

    for i in range(len(pizza)):
        # [pizza 번호, 치즈 양] 순서표를 붙혀줌
        pizza_line.append([i+1, pizza[i]])

    # 화덕
    queue = []

    # 시작만큼 채워줌
    for i in range(N):
        queue.append(pizza_line.pop(0))


    while queue:
        cur_pizza = queue.pop(0)
        cur_pizza[1] //= 2
        if cur_pizza[1] == 0:
            if pizza_line:
                queue.append(pizza_line.pop(0))
        else:
            queue.append(cur_pizza)


    print("#{} {}".format(tc,cur_pizza[0]))