import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    min_value = numbers[0]

    for i in range(1,n):
        if numbers[i] > max_value:
            max_value = numbers[i]

        if numbers[i] < min_value:
            min_value = numbers[i]

    print("#{} {}".format(tc, max_value - min_value))