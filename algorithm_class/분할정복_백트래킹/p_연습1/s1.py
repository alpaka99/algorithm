"""
연습 문제1. 정렬 복습 - 정렬1
"""
#1. 버블 정렬
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] >= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
bubble_sort(bubble_nums)
print(bubble_nums)

#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)-1):
        min_val = nums[i+1]
        min_idx = i+1
        for j in range(i+1, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j
        if nums[i] > min_val:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]




selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
selection_sort(selection_nums)
print(selection_nums)

#3. 카운팅 정렬
def counting_sort(nums):
    max_val = nums[0]
    for i in range(len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]

    cnt_list = [0 for _ in range(max_val+1)]

    for i in range(len(nums)):
        cnt_list[nums[i]] += 1

    result = []
    for i in range(len(cnt_list)):
        for j in range(cnt_list[i]):
            result.append(i)
    return result


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
answer = counting_sort(counting_nums)
print(*answer)