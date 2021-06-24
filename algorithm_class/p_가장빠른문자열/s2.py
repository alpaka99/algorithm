import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

def speed_typing(tat, pat):

    # 
    pp = 0
    # target의 index를 가르키는 포인터
    pt = 0

    cnt = 0

    # brute force로 패턴이 몇개 있는지 구해주자
    while pt < len(tat):
        # 여기가 패턴이 맞는지 틀린지 검사
        # 하나가 같으면 else에서 초기화를 안하고 쭉 검사
        if tat[pt] == pat[pp]:
            pt += 1
            pp += 1
        # 다르면 pp를 0으로 초기화해주고 pt는 다시 돌아가서 1 증가시켜줌
        else:
            pt = pt - pp + 1
            pp = 0

        # 만약 패턴이 맞으면
        if pp == len(pat):
            # 지금까지 검사한 바로 뒤로 pt 포인터를 옮겨줌
            #pt += 1
            # 그리고 pp는 초기화
            pp = 0
            cnt += 1

    answer = len(tat) - len(pat) * cnt + cnt
    # (타겟의 길이 - 패턴 길이 * 타겟있는 횟수 + 타겟 있는 횟수)
    return answer

T = int(input())

for tc in range(1, T+1):
    tat, pat = map(str, input().split())
    print('#{} {}'.format(tc, speed_typing(tat, pat)))