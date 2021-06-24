import sys
sys.stdin = open('input.txt', 'r')


def terminate(level, max_length):
    # 파리채처럼 잘라서 해당 범위안에 tumor가 몇개있는지
    max_tumor_kill = 0

    for i in range(max_length-level+1):
        for j in range(max_length-level+1):
            tumor_kill = 0
            for tumor in tumors:
                # start = [i,j]
                # end = [i+level,j+level]
                if i<= tumor[0] <= i + level and i<= tumor[2] <= i + level:
                    if j <= tumor[1] <= j + level and j <= tumor[3] <= j + level:
                        tumor_kill += 1

            if tumor_kill > max_tumor_kill:
                max_tumor_kill = tumor_kill

    return (level, max_tumor_kill)


for tc in range(1, int(input())+1):
    # 종양수 N, M개 이하로 종양을 줄여야함
    N, M = map(int, input().split())

    k = 0
    tumors = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0
    for tumor in tumors:
        #print(tumor)
        tmp_max = max(tumor)
        if tmp_max > max_length:
            max_length = tmp_max
    #print(max_length)
    min_level = max_length
    for i in range(1, max_length):
        length, tumor_kill = terminate(i,max_length)

        if N-tumor_kill <= M:
            if length < min_level:
                min_level = length
                #print(N-tumor_kill)
    print("#{} {}".format(tc,min_level))
