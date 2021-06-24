import sys
sys.stdin = open("input.txt","r")

for tc in range(1,11):
    dump = int(input())
    boxes = list(map(int,input().split()))

    chance = 0
    while chance < dump:
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        chance += 1
    result = boxes[max_idx] - boxes[min_idx]
    print("#{} {}".format(tc,result))