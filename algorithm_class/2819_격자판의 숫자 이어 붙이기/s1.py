import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 4 by 4 matrix
    matrix = [list(map(int, input().split())) for _ in range(4)]
    
    # 임의의 위치에 시작해서 4방향으로 이동