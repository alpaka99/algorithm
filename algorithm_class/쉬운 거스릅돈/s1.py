import sys
sys.stdin = open("input.txt", "r")

# T: test case
# N: 거슬러 주어야할 금액

for tc in range(1,int(input())+1):
    # 거스름돈 리스트를 만들자
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 거스름돈 몇개를 줬는지 저장하는 리스트
    count = [0]*len(changes)
    # 거슬러 줘야할 돈
    n = int(input())

    # runtime error 뭐지...
    # 생각하는 방식을 바꿔야하는데 어떡해야하려나...
    # for문으로 돌리면서 while로 그때그떄 최대치만큼 빼주는 방법?
    # 뭐지? 이게 왜 런타임이 훨씬 빠르지? if를 적게 사용해서 그런가?
    
    # 현재까지 준 잔돈의 액수
    cur_sum = 0
    
    # for문을 통해 changes의 인덱스에 하나씩 접근
    for i in range(len(changes)):
        # 만약 거스름돈을 더했는데도 줘야할 값보다 작으면 계속 while문이 돌아감ㄴ
        while n >= cur_sum + changes[i]:
            # 만약 거스름돈이 정확하게 맞으면 while문을 빠져나감
            if cur_sum == n:
                break
            # 더해도 줘야할 돈보다 작으므로 더하고 count의 해당 칸에도 1 올림
            cur_sum += changes[i]
            count[i] += 1
        #거스름돈이 같으면 for문도 빠져나가야함으로 break 한번 더
        if cur_sum == n:
            break

    print("#{}".format(tc))
    for i in range(len(count)):
        print("{}".format(count[i]), end=' ')
    print()

