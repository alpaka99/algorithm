import sys
sys.stdin = open('input.txt', 'r')

# 그냥 머릿속에 갑자기 떠오른 방법
# 이러면 여러번 돌면서 list의 값을 일일히 변경 안해도 됨
# 근데 내가 원하던 방법은 아님
for tc in range(1, int(input())+1):
    original = input()

    count = 0
    # 몇번 0,1로 바뀌는지만 세어서 결과 출력
    for i in range(1,len(original)):
        # 만약 이전과 현재의 비트가 다르면 count에 1 증가
        if original[i-1] != original[i]:
            count += 1
    # 처음이 1이면 맨 처음에도 한번 바꿔줘야하므로 1 또 증가
    if original[0] == '1':
        count += 1
    print("#{} {}".format(tc,count))