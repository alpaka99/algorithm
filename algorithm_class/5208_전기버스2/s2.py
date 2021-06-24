import sys
sys.stdin = open('input.txt', 'r')
global min_val

def recursive(N:int, fuel:int, pos:int, cnt:int):
    global min_val
    if pos >= N:
        min_val = min(min_val, cnt)

    if cnt >= min_val:
        return

    for i in range(pos, pos+fuel):
        if not(visited[i]):
            visited[i] = 1
            fuel += bus_stop[i]- (i-pos)
            recursive(N,fuel+bus_stop[i],i,cnt+1)
            fuel -= bus_stop[i] - (i - pos)
            visited[i] = 0


for tc in range(1, int(input())+1):
    data = list(map(int, input().split()))
    N = data[0]
    bus_stop = data[1:]+[0]
    min_val = 100*N
    visited = [0 for _ in range(N+1)]

    recursive(N,1,0,0)

    print("#{} {}".format(tc,min_val-1))