# 6개의 원소가 담긴 리스트
nums = [3, 6, 7, 1, 5, 4]
# 리스트의 크기
n = len(nums)
# 부분집합의 개수를 더해 갈 변수
cnt = 0

# 모든부분집합의 갯수만큼 반복
for i in range(1<<n):
    cnt += 1
    # 리스트의 원소 개수만큼 반복
    # j는 부분집합의 원소를 가져갈 idx에 해당됨
    for j in range(n):
        if i & (1<<j):
            print(nums[i],end = ' ')
        print()
print(cnt)