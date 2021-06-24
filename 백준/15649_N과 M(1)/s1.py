import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations

N, M = map(int, input().split())

a = [i for i in range(1, N+1)]

b = list(permutations(a,M))

for tup in b:
    print(*tup)


