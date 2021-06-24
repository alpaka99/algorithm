# 격자 각 칸은 5종류중 하나
# 각 종류들은 서로서로 연결되어 있어야함
# 한 종류에서 인접한 다른 종류로 갈 수 있음 -> 두 종류는 연결되어있다.

#(d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
def partition(N):
    ans = []
    for x in range(1, N+1):
        for y in range(2, N+1):
            for d1 in range(1, N+1):
                for d2 in range(1, N+1):
                    if d1 + d2 + x <= N and 1 <= y - d1 and y + d2 <= N:
                        ans.append([x,y,d1,d2])
    return ans

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):

    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]



    # 나누는 방법
    # 1. 기준점과 경계의 길이를 정한다.(d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
    # 2. 경계선을 쭉 그린다
    # 3. 경계선과 경계선의 안에 포함되어있는곳은 5번 선거구
    # 4. 각 선거구
    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    # -> 그러면 각 선거구를 그리고 안에 다시 5번 선거구를 그리는게 나을듯



    # 자 이제 선거구를 나눠야하는디...
    # 자 이제 x, y, d1, d2를 어캐 구한다냐...
    tmp = partition(N)

    # flag_1 ... flag_5 까지 다 true인 애들 저장
    real_divided = []
    while len(tmp):
        # 여기까지는 생각대로
        x, y, d1, d2 = map(int,tmp.pop())

        # 선거구를 나눠야함
        divided = [[0] * N for _ in range(N)]

        # 이제 구역을 x,y,d1,d2에 따라 나누자
        # 안칠해진 선거구 확인
        flag_1 = False
        flag_2 = False
        flag_3 = False
        flag_4 = False

        # 1번 선거구
        for i in range(x+d1):
            for j in range(y):
                divided[i][j] = 1
                flag_1 = True

        # 2번 선거구
        for i in range(x+d2):
            for j in range(y,N):
                divided[i][j] = 2
                flag_2 = True

        # 3번 선거구
        for i in range(x+d1-1, N):
            for j in range(y-d1+d2):
                divided[i][j] = 3
                flag_3 = True

        # 4번 선거구
        for i in range(x + d2, N):
            for j in range(y-d1+d2-1, N):
                divided[i][j] = 4
                flag_4 = True

        # 5번 선거구
        # 우선 경계선을 그리자
        p1 = [x-1,y-1]
        l = 0
        # 왼.위 그리기
        while l <= d1:
            divided[p1[0]][p1[1]] = 5
            p1[0] += 1
            p1[1] -= 1
            l += 1
        #오.위 그리기
        p1 = [x-1, y-1]
        l = 0
        while l <= d2:
            divided[p1[0]][p1[1]] = 5
            p1[0] += 1
            p1[1] += 1
            l += 1
        # 왼.아 그리기
        p1 = [x-1+d1,y-1-d1]
        l = 0
        while l <= d2:
            divided[p1[0]][p1[1]] = 5
            p1[0] += 1
            p1[1] += 1
            l+=1
        # 왼.아 그리기
        p1 = [x - 1 + d2, y - 1 + d2]
        l = 0
        while l <= d1:
            divided[p1[0]][p1[1]] = 5
            p1[0] += 1
            p1[1] -= 1
            l+=1

        # 경계선은 그렸으니까 이제 5로 그 사이를 칠하자
        stack = []
        for i in range(N):
            flag_5 = False
            tmp_stack = []
            # 백트랙킹 용
            for j in range(N):
                # 5를 만난적이 없다
                if flag_5 == False:
                    if divided[i][j] == 5:
                        flag_5 = True
                    # 5를 만난적이 있다
                else:
                    # 5를 다시 만난다? -> 칠하기 끝
                    if divided[i][j] == 5:
                        flag_5 == False
                        stack += tmp_stack
                    # flag_5가 True인데 5를 다시 만나지 않음->append
                    else:
                        tmp_stack.append([i,j])
        # 사이에 있는것들을 다 구했으니까 칠하자
        flag_5 = False
        while stack:
            tmp_5 = stack.pop()
            divided[tmp_5[0]][tmp_5[1]] = 5
            flag_5 = True

        #
        if (flag_1 == True) and (flag_2 == True) and (flag_3 == True) and (flag_4 == True) and (flag_5 == True):
            real_divided.append(divided)
            pass

    ########## while문 끝 ############
    # 다 하고나서 연산
    max_sub_min = 100*20*20


    while real_divided:
        # 각 선거구 별 인원 저장
        population = [0] * 6

        max_pop = 0
        min_pop = 100*20*20

        divided = real_divided.pop()
        for i in range(N):
            for j in range(N):
                population[divided[i][j]] += matrix[i][j]

        population.pop(0)
        for i in range(5):
            if population[i] > max_pop:
                max_pop = population[i]
            if population[i] < min_pop:
                min_pop = population[i]

        if max_sub_min > max_pop - min_pop:
            max_sub_min = max_pop - min_pop

    print("#{} {}".format(tc,max_sub_min))