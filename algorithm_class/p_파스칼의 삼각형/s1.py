import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 파스칼 삼각형의 크기
    N = int(input())
    
    # 현재 위에서부터의 레벨
    level = 1

    # 스택에 시작값 1을 넣어줌
    stack = []
    stack.append(1)

    print("#{}".format(tc))

# pascal 삼각형의 level이 N에 도달할때까지 계속 진행
    while level <= N:
        # 해당 레벨에 맞는 tmp 배열을 0으로 초기화해서 준비
        # +1을 해주는 이유는 다음 레벨의 배열을 만드는것이기 때문에
        tmp = [0]*(level+1)
        # 현재 stack에서 pop할 값을 더할 위치를 나타내는 pos
        pos = 0
        # 이전 레벨의 값들이 stack에 들어있음
        while len(stack):
            # 값 하나를 pop함
            num = stack.pop()
            # pop한 값을 위치에서 바로 아랫값이랑 그 오른쪽값에 더함
            tmp[pos] += num
            tmp[pos+1] += num
            # 그리고는 position을 한칸 이동시켜줌
            pos += 1
        #성공적으로 다 더하면 level을 1 증가시켜서 다음 레벨을 준비
        level += 1
        # 현재 tmp값이 다음레벨에서는 stack의 값으로 쓰임
        # -1 전까지 slicing 해주는 이유는
        # 1. 가장 첫 레벨에 1, 1 이렇게 되는것을 방지
        # 2. 1을 방지하기위해 넣은 0을 뒷 레벨들에서는 잘라줌
        stack = tmp[:-1]
        print(*tmp[:-1])
