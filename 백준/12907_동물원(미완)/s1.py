import sys
sys.stdin = open('input.txt', 'r')

for _ in range(int(input())):
    N = int(input())

    animals = list(map(int, input().split()))
    max_len = max(animals)
    count = [0 for _ in range(N)]

    for i in range(N):
        if animals[i] > N:
            print(0)
            break
        count[animals[i]] += 1
    print(count)
    # 이 count에 들어있는게 뒤로 갈 수록 숫자가 작아지는 식으로 들어있는지 확인하고
    # 그 때에 가장 마지막보다 앞까지 2의 제곱을 하면 될듯
    # count가 이상한경우는 0