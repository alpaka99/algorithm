import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
road = list(map(int, input().split()))

def dp(pos:int, val:int):
    if pos >= N:
        return 0
    val += road[pos]
    a = dp(pos+2,val)
    b = dp(pos+7,val)

    return val+max(a,b)

print(dp(0,0))