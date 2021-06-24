"""
연습문제 4. 부분 집합의 합 구현

4-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기

** 비트 연산
- 원소 수에 해당하는 N개의 비트열을 활용
- n번째 비트값이 1이면 n번째 원소가 '포함'되었음을 의미

0   0 0 0 0   {A, B, C, D}
1   0 0 0 1   {A}
2   0 0 1 0   {B}
3   0 0 1 1   {B, A}
...........
14  1 1 1 0   {D, C, B}
15  1 1 1 1   {D, C, B, A}
"""

#1. 재귀 활용
def recursive_powerset(N:int, num_set:set):
    tmp = []
    for i in range(N):
        if visited[i] == '1':
            tmp.append(nums[i])
    if sum(tmp) == 0:
        print(*tmp)

    # 트리에서 가지치기한다는 개념으로 접근해야해
    # 근데 가지 아래에 또 가능성이 있을 수 있으니까 다 해봐야겠다.
    for i in range(N):
        bin_visited = ''.join(visited)
        if bin_visited not in num_set:
            visited[i] = '1'
            num_set.add(bin_visited)
            recursive_powerset(N, num_set)
            visited[i] = '0'
            num_set.pop(bin_visited)


#2. 비트 연산 활용
def bit_powerset(nums:list, N:int):
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i & (1<<j):
                tmp.append(nums[j])

        if sum(tmp) == 0:
            print(*tmp)



nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)

bit_powerset(nums,N)
print('################# bit power set ################')

visited = ['0' for _ in range(len(nums))]

num_set = set()
recursive_powerset(N, num_set)