import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
op_list = []
for i in range(4):
    while op[i]:
        op[i] -= 1
        op_list.append(i)

op_orders = list(permutations(op_list, len(op_list)))

for op_order in op_orders:
    pass