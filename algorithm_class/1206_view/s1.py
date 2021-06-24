import sys
# sys.stdin = open('input.txt')
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    num = int(input())
    bd = list(map(int,input().split()))

    # 각자 주위 가장 높은 타워의 위치를 기록
    close_bd = [0]*num

    for i in range(len(bd)):
        if bd[i]:
            # 왼쪽 오른쪽 초기화
            left_height = 0
            right_height = 0

            #왼쪽 검증
            #왼쪽 두 집중 가장 높은거 저장
            if bd[i-1] > bd[i-2]:
                left_height = bd[i-1]
            else:
                left_height = bd[i-2]

            #오른쪽 검증
            # 오른쪽 두 집중 가장 높은거 저장
            if bd[i+1] > bd[i+2]:
                right_height = bd[i+1]
            else:
                right_height = bd[i+2]

            # 둘중에 더 높은 빌딩 높이를 저장
            if left_height > right_height:
                close_bd[i] = left_height
            else:
                close_bd[i] = right_height
            
    # 조망권 확보된 층이 어딨는지를 알기 위해 주위 가장 높은층을 빼줌
    for i in range(len(bd)):
        bd[i] = bd[i] - close_bd[i]

    # 조망권 확보된 층 다 더하기
    result = 0
    for num in bd:
        if num > 0:
            result += num

    print("#{} {}".format(tc,result))