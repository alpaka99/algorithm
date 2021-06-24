import sys
sys.stdin = open("input.txt", "r")

# 가로의 길이는 항상 100
# 상자 높이는 1 이상 100 이하
# 덤프 횟수는 1 이상 10000 이하
# 총 10개의 test case
# 첫번째 줄에는 덤프 횟수,
# 다음줄에 상자의 높이 값들

for tc in range(1, 11):
    dump_num = int(input())
    boxes = list(map(int,input().split()))

    # 어떻게 풀까
    # 매 반복마다 최고점과 최저점을 찾아서
    # 더해주고 빼주는게 제일 편할것 같음

    # 덤프 횟수만큼 반복
    for _ in range(dump_num):
        max_value = 0
        max_idx = 0
        min_value = 100
        min_idx = 0

        # 최고점, 최저점 찾기
        for i in range(len(boxes)):
            if boxes[i] > max_value:
                max_idx = i
                max_value = boxes[i]

            if boxes[i] < min_value:
                min_idx = i
                min_value = boxes[i]

        # 최고점에서 최저점으로 dump
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    # 출력전 마지막으로 최고점이랑 최저점 찾기
    max_value = 0
    min_value = 100
    for i in range(len(boxes)):
        if boxes[i] > max_value:
            max_value = boxes[i]

        if boxes[i] < min_value:
            min_value = boxes[i]
    print("#{} {}".format(tc, max_value - min_value ))