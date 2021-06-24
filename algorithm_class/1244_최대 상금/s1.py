import sys
sys.stdin = open('input.txt', 'r')


global max_val

def permutation(swap_count:int):
    global max_val
    # 재귀 탈출 조건
    if swap_count == 0:
        result = int(''.join(nums)) # 이런 예쁜 방법이 있었다니
        if result > max_val:
            max_val = result
        return

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i] # 어떤 두 수를 바꿔주고
            swap_count -= 1 # swap count를 1 감소
            tmp = int(''.join(nums))
            if tmp in visited: # 만약 해당 수가 set에 없다? -> 새롭게 도전할 만한 branch다!
                pass
            else:
                visited.append(tmp)
                permutation(swap_count)
            swap_count += 1  # 이것도 원상 복구
            nums[i], nums[j] = nums[j], nums[i] # permutation 재귀가 끝났으니 원상 복구




for tc in range(1, int(input())+1):
    # 숫자판, 교환 횟수
    num, N = map(str, input().split())

    # str로 된 숫자들을 list의 한칸한칸으로 바꿔줌
    nums = list(num)

    # 몇번 바꿀건지 count해주는 변수
    # swap_count를 여기서 설정해주는 방법은 상상도 못했다... ㅠ
    swap_count = int(N)

    # 한번 갔으면 또 안가도 되니까 이 set에 해당 번호가 있는지 없는지 추후 검색
    # num_set = set()
    visited = []
    # 최댓값인지 측정하는 변수
    max_val = 0

    permutation(swap_count)

    print("#{} {}".format(tc,max_val))


