N = 3
arr = [1, 2, 3] # 구하고자 하는 부분 집합
sel = [0] * N # a 리스트 (내가 해당 원소를 뽑았는지 체크하는 리스트)

def powerset(idx):
    for i in range(3):
        if sel[i] == 0:
            sel[i] = 1
            print(arr[i], end='')
            powerset(i)
            sel[i] = 0

    print()

powerset(0)