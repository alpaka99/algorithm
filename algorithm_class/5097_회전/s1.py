import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())



    queue = list(map(int,input().split()))

    for _ in range(M):
        queue.append(queue.pop(0))

    print("#{} {}".format(tc,queue[0]))