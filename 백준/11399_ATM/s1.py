import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
time = list(map(int, input().split()))

time.sort()
for i in range(len(time)-1):
    time[i+1] += time[i]
print(sum(time))
