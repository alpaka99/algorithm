import sys
sys.stdin = open("input.txt", "r")

def dump(n, numbers):
    # 최고 숫자와 최저 숫자 찾기

    count = n

    while count > 0:
        max_n = numbers[0]
        min_n = numbers[0]
        # print(max(numbers))
        for i in range(len(numbers)):
            if max_n < numbers[i]:
                max_n = numbers[i]
        for j in range(len(numbers)):
            if min_n > numbers[j]:
                min_n = numbers[j]
            # 최고 숫자에서 -1 최저 숫자에서 + 1
        for k in range(len(numbers)):
            if numbers[k] == max_n:
                numbers[k] -= 1
                break

        for l in range(len(numbers)):
            if numbers[l] == min_n:
                numbers[l] += 1
                break

        count -= 1
        # print(count)
        # print(numbers)

        max_n = 0
        min_n = 100
        for i in range(len(numbers)):
            if max_n < numbers[i]:
                max_n = numbers[i]

        for j in range(len(numbers)):
            if min_n > numbers[j]:
                min_n = numbers[j]

    return max_n - min_n

for i in range(10):
    n = int(input())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(i+1,dump(n, numbers)))