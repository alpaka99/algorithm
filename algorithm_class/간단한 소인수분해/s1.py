import sys
sys.stdin = open("input.txt", "r")


# T: 테스트 케이스
# 아래로 T개의 테스트 케이스가 주어짐
# 각 줄의 첫번째 줄에 N이 주어짐

# T 따로 안만들어봄
for tc in range(1, int(input())+1):
    n = int(input())

    # n의 약수들의 모음
    divs = [2, 3, 5, 7, 11]

    # 해당 약수가 몇번 쓰였는지 count하는 list
    count = [0]*5

    # divs의 각 칸마다 돌면서 나눠보고
    # 나눠지면 count의 해당칸을 1 올리고
    # 안나눠지면 나와서 다음 수로 나눠봄
    # 잠만 근데 여러번 나뉠 수 도 있자나
    # 그럼 while?

    i = 0
    while i < len(divs):
        # 안나눠지면 i를 1 증가시켜서 divs안에 있는 다음 수가 나누게 해봄
        if n % divs[i]:
            i += 1
        # 나눠지면 해당 count list칸을 1 증가하고 n을 진짜 나눠줌
        else:
            count[i] += 1
            n //= divs[i]

    print("#{}".format(tc), end=" ")
    for i in range(len(count)):
        print("{}".format(count[i]),end=" ")

    print()

