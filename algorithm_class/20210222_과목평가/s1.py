import sys
sys.stdin = open('input1.txt', 'r')
# 2. 함수 구현
def gardening(N, M, garden):

    # 2.1 out 할 값들
    tree_pay = 0 # 나무의 총 가격
    tree_cnt = 0 # 심은 나무 수
    expensive_tree = 0 # 가장 비싼 나무의 가격
    expensive_tree_col = 0 # 가장 비싼 나무가 심어진 열​
    # 2.2 열고정 행순회이며, 짝수 열 인덱스의 값만 더해줘야 한다. 인덱스는 0부터 시작하기 때문!
    # range(start,end,step)을 이용하자
    # 열고정 행순회이기 때문에 열을 바깥 for 문에 작성한다.
    for i in range(0, M, 2):
        # 행 순회를 안쪽 for문에 작성한다.
        for j in range(N):
            # 위에서 열의 범위 자체를 짝수인덱스 열로 처리했기때문에 tree_pay와 tree_cnt를 위해 조건문은 없다.
            tree_pay += garden[j][i]
            tree_cnt += 1
            # 최대값과 그때 열의 인덱스 구하기
            # 최대값이 중복일 경우 더 큰 열인덱스를 반환해야 하므로, 등호를 삽입한다.
            # 최대값이 중복일 경우 더 큰 열인덱스를 반환해야 한다면, 등호를 빼야한다.
            if garden[j][i] >= expensive_tree:
                expensive_tree = garden[j][i]
                # 인덱스는 0부터 시작인데, 출력은 1~M으로 해야해서 1을 더해준다
                expensive_tree_col = i + 1

    # 2.3 모든 반복문이 종료된 후 4개의 출력값을 한줄로 묶어서 출력해야하기 때문에
    # join을 쓰기 위해 각 요소를 int가 아닌 str로 만들기 위해 map을 사용한다.
    return ' '.join(map(str, [tree_pay, tree_cnt, expensive_tree, expensive_tree_col]))


# 1.input 받기
for tc in range(1, int(input())+1):
    # 1.1 정원의 가로, 세로
    N, M = map(int, input().split())
    # 1.2 정원에 심을 나무들의 가격
    garden = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, gardening(N, M, garden)))