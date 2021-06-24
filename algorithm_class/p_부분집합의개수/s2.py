import sys
sys.stdin = open('input.txt', 'r')

# 1번째 포인트
# 1부터 12까지의 숫자를 원소로 가진 집합 A
A = [i for i in range(1, 13)]

# tc 입력받고
for tc in range(1, int(input())+1):
    # N은 부분집합의 원소의 갯수
    # K는 부분집합 원소의 총 합
    N, K = map(int,input().split())
    
    # 최종적으로 출력할 변수
    # 조건에 부합하는 부분집합이 없으면 0을 출력
    ans = 0
    
    # 총 부분 집합의 갯수 만큼 반복
    for i in range(1 << len(A)):
        # 매 반복마다 몇개의 원소인 부분집합인지, 합이 얼마인지 초기화
        bit_sum = 0
        num_sum = 0
        # A의 각 요소에 접근
        for j in range(len(A)):
            if i & (1<<j):
                bit_sum += 1
                num_sum += A[j]
        # 2, 3번째 포인트
        if bit_sum == N and num_sum == K:
            ans += 1
    print("#{} {}".format(tc, ans))