import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    unsorted = list(map(int, input().split()))

    # 이동을 담당하는
    pos = 0
    # 비교를 담당하는
    compare = 1
    # 최대를 찾는지 최소를 찾는지 결정해주는
    max_flag = True
    
    # 가장 끝 앞에까지해야 index error가 안남
    while pos < 10:
        # 최대를 찾아야 하는 상황
        if max_flag:
            # 비교하는게 unsorted의 마지막에 도착할때까지 비교를 진행
            while compare <= N-1:
                # 만약 뒤에 더 큰게 있으면 가장 앞에 있는거랑 바꿔줌
                if unsorted[pos] < unsorted[compare]:
                    unsorted[pos], unsorted[compare] = unsorted[compare], unsorted[pos]
                # 다음것과 비교하기 위해 compare를 1 증가
                compare += 1
            # while을 다 하고 나오면
            # 1. max_flag를 False로 만들어서 다음번에는 최솟값을 찾게 해줌
            max_flag = False
            # 2. 비교할 기준이 되는 칸을 뒤로 한칸 이동시킴
            pos += 1
            # 3. 비교를 시작할 부분을 기준이 되는 칸 1로 다시 만듬
            compare = pos + 1

        # 최소를 찾아야하는상황
        else:
            while compare <= N - 1:
                if unsorted[pos] > unsorted[compare]:
                    unsorted[pos], unsorted[compare] = unsorted[compare], unsorted[pos]
                compare += 1
            # while을 다하고 나오면
            max_flag = True
            pos += 1
            compare = pos + 1
    print("#{}".format(tc), *unsorted[:10])