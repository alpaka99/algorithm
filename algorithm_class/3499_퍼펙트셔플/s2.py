import sys
sys.stdin = open('input.txt', 'r', encoding='utf8')

for tc in range(1, int(input())+1):
    N = int(input())
    words = list(input().split())
    
    # 홀수면 더미 데이터를 1개 넣어줌
    odd_flag = False
    if len(words)%2:
        words.append("dummy")
        odd_flag = True
        N = len(words)
    half = N//2

    # 어쩃거나 짝수일때의 정렬
    i = 0
    ans = []
    while i < half:
        ans.append(words[i])
        ans.append(words[i+half])
        i += 1

    # 만약 홀수였으면 짝수의 마지막번인 dummy를 pop해줌
    if odd_flag == True:
        ans.pop()

    print("#{}".format(tc),*ans)