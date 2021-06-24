import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스의 갯수 : 10
N = int(input())
# 비어있는 리스트 (최대값을 담을 리스트)


# 두개의 길이가 다른 리스트에서 짧은 리스트를 움직여가며 곱했을 때 최대값을 찾아주는 리스트
def find_max(max_value_list,list1, list2):
    # 리스트 인덱스 변수
    i = j = 0
    # 최대값 변수
    max_value = 0

    #2번 리스트가 더 길스 경우 동일 인덱의 수끼리 곱한 뒤 빈 리스트에 넣고 1번 리스트의 맨 앞에 '0'을 추가해 동작 반복(재귀)
    if len(list1) < len(list2):
        while i <= len(list1) - 1:
            max_value += list1[i] * list2[j]
            i += 1
            j += 1
        max_value_list.append(max_value)
        if len(list1) < len(list2):
            list1.insert(0, 0)
            return find_max(max_value_list, list1, list2)
        else:
            return max(max_value_list)

    # 리스트의 길이가 서로 같을 경우 빈 리스트에 곱한 값을 넣고 그 중 최대값 return (재귀 함수이기에 결국 이 동작 진행됨)
    elif len(list1) == len(list2):
        while i <= len(list1) - 1:
            max_value += list1[i] * list2[j]
            i += 1
            j += 1
        max_value_list.append(max_value)
        return max(max_value_list)

    # 위와 반대의 경우 2번 리스트의 맨 앞에 0을 넣고 동작 재수행
    else:
        while j <= len(list2) - 1:
            max_value += list1[i] * list2[j]
            i += 1
            j += 1
        max_value_list.append(max_value)
        if len(list1) > len(list2):
            list2.insert(0, 0)
            return find_max(max_value_list, list1, list2)
        else:
            return max(max_value_list)

for tc in range(1, N+1):
    n = input()
    max_value_list = []
    numbers_list1 = list(map(int, input().split()))
    numbers_list2 = list(map(int, input().split()))


    print(find_max(max_value_list, numbers_list1, numbers_list2))