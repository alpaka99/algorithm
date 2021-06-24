def solution(n, k):
    if n == k:
        print(*nums)
    else:
        for i in range(n,k):
            nums[i], nums[n] = nums[n], nums[i]
            solution(n+1, k)
            nums[i], nums[n] = nums[n], nums[i]

nums = [1, 2, 3]
solution(0,3)