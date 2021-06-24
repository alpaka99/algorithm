#연산자 우선순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
# N개의 숫자에 +,-,x,/를 끼워넣어 다양한 값

# 최대값 - 최소값
def operator_powerset(history:list):
    if len(history) == N-1:
        tmp = history[:]
        powersets.append(tmp)
        return

    for i in range(4):
        if visited[i] != 0:
            visited[i] -= 1
            history.append(operator[i])
            operator_powerset(history)
            history.pop()
            visited[i] += 1

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return int(a/b)

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    operator = ['+', '-', '*', '/']
    op_dict = {'+':add, '-':sub, '*':mul, '/':div}
    operator_num = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # 이건 ㄹㅇ 순열조합 아님?
    powersets = []
    visited = operator_num[:] # 하나 쓸 떄마다 하나 뺄 예정

    operator_powerset([])

    results = []


    i = 0
    while i < len(powersets):
        cur_opset = powersets[i]
        j = 0
        answer = numbers[0]
        for j in range(N-1):
            cur_operator = cur_opset[j]
            answer = op_dict[cur_opset[j]](answer, numbers[j + 1])
        results.append(answer)
        i += 1

    max_val = results[0]
    min_val = results[0]

    # print(numbers)
    # print(powersets)
    # print(results)
    for i in range(len(results)):
        if max_val  < results[i]:
            max_val = results[i]
        if min_val > results[i]:
            min_val = results[i]


    print('#{} {}'.format(tc,max_val - min_val ))