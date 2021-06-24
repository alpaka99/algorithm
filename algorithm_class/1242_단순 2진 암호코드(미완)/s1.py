import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # 암호 코드 = 7자리 + 검증코드 1자리 = 8자리
    # 검증코드 규칙이 있음


    # 세로 50 가로 100 이하의 암호코드들이 저장
    # 정상적인 암호코드면 출력
    code = [int(input()) for _ in range(N)]
    print(code)