import sys
sys.stdin = open('input.txt', 'r')

# 문제에서의 cycle을 돌려주는 함수
def cycle(queue):
    for i in range(1, 6):
        tmp = queue.pop(0)
        tmp -= i # 맨앞의 값을 해당하는 cycle의 값 만큼 뺴줌
        if tmp <= 0: # 만약 뺀 값이 0보다 작거나 같으면
            queue.append(0)
            return 0
        queue.append(tmp)
    return 1 # 사이클에서 0이 발견되지 않았음


for _ in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))

    # cycle함수에서 0이 return 될 때 까지 계속 돔
    while cycle(queue):
        pass
    
    # while loop 탈출
    print("#{}".format(tc),*queue)