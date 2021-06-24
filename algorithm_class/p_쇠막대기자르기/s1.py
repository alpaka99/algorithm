import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,int(input())+1):
    ans = 0
    steel = input()

    
    # 현재 steel에서 보고 있는 위치
    pos = 0
    left_count = 0
    left_flag = 0
    right_flag = 0

    while pos < len(steel):
        # 일단 pos의 위치를 봄
        if steel[pos] == '(':
            left_count += 1
            left_flag = 1
        else:
            right_flag = 1


        # 봤는데 괄호가 왼쪽 오른쪽 연달아 나왔음
        # laser라는 뜻
        if left_flag == 1 and right_flag == 1:
            # 다음에 뭐가 나올지 모르니까 일단은 초기화 시켜줌
            left_flag = 0
            right_flag = 0
            # laser는 현재 아래에 있는 쇠막대기를 다 1씩 늘려주는 효과
            left_count -= 1
            ans += left_count
            # 아래 오른쪽 괄호만 나왔을때의 연산을 피하기 위해서 continue


        # 만약 오른쪽 괄호만 나왔으면
        if right_flag == 1:
            left_count -= 1
            ans += 1
            # )( 경우를 방지해주기 위해서
            right_flag = False
        pos += 1

    print("#{} {}".format(tc,ans))