"""
연습문제 4. 부분 집합의 합 구현

4-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def powerset(nums:list, N:int):
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                print(nums[j], end=' ')
        print()

nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# nums = [1, 2, 3, 4]
N = len(nums)
powerset(nums, N)