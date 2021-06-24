# 1에서 5가 담긴 리스트
arr = [ i for i in range(1, 6)]

# 부분집합의 갯수만큼 반복
for i in range(1<<len(arr)):
    for j in range(len(arr)):
        if i & (j<<1):
            print(arr[i], end = '')