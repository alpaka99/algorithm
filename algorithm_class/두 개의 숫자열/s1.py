import sys
sys.stdin = open("input.txt", "r")


# T는 테스트 케이스
# 두 배열의 길이 N, M
# 세번째 줄에는 An의 내용물
# 네번째 줄에는 Bn의 내용물
def check_n_swap(a,b):
    if len(a) > len(b):
        tmp = a[:]
        local_a = b[:]
        local_b = tmp
        return local_a, local_b
    else:
        return a, b

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    list_a = list(map(int,input().split()))
    list_b = list(map(int,input().split()))
    
    # 일단 둘 중 어느게 더 긴지 알아야함
    # check and swap 함수를 만들어보자

    list_a, list_b = check_n_swap(list_a, list_b)
    # print(lists)
    # list_a = lists[0]
    # list_b = lists[1]
    # list_a가 더 짧은 배열, list_b가 더 긴 배열

    # 구간합 때 사용한 방법으로 진행
    max_value = 0
    for i in range(len(list_b)-len(list_a)+1):
        cur_value = 0
        # i번 index부터 list_a의 길이만큼
        for j in range(len(list_a)):
            cur_value +=  list_a[j]*list_b[i+j]
        # 매 window screen마다 max_value와 곱한것들의 합을 비교
        if max_value < cur_value:
            max_value = cur_value
    print("#{} {}".format(tc,max_value))
    

