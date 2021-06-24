import sys
sys.stdin = open('input.txt', 'r')

class human:
    # 클래스 변수로 좌우상으로 선언해줌
    # 이래야 좌,우 먼저 보고 위로 가는길을 그 다음에 봄
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    
    # __init__ 매서드, x, y, map을 지정
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map

    # self.map을 보고 길을 찾는 navigation method
    # 주위를 둘러봐서 길이 있으면 해당 길의 좌표를 반환
    def navigate(self):
        for i in range(3):
            nx = self.x + self.dx[i]
            ny = self.y + self.dy[i]
            # 만약 주위의 길을 봤을때 길이 있으면 해당 좌표를 반환
            if self.map[nx][ny] == 1:
                return nx, ny


    # navigate() 메서드를 통해서 얻은 길의 좌표로 걸어가는 메서드
    def walk(self):
        nxt = self.navigate()
        # 왔던 길을 0으로 칠해줘야 다시 안돌아감
        self.map[self.x][self.y] = 0
        # 객체의 위치를 이동시켜줌
        self.x = nxt[0]
        self.y = nxt[1]

    # 현재 자신의 위치를 반환해주는 cur_location() 메서드
    def cur_location(self):
        return self.x, self.y

# 지정된 도착지점(2)에 도달하는 시작점의 x좌표를 구하라
for tc in range(1, 11):
    N = int(input())

    # 양쪽에 0을 더해줘서 index error를 방지(다은님 아이디어 차용)
    matrix = [([0] + (list(map(int, input().split()))) + [0])  for _ in range(100)]


    # 난 거꾸로 올라갈꺼야
    for col in range(101):
        if matrix[99][col] == 2:
            # 도착점인 2가 들어있는곳의 좌표를 시작점으로 저장
            cur_x ,cur_y = 99, col

    
    # human 클래스의 객체 하나 생성
    seokhwan = human(cur_x, cur_y, matrix)

    # 객체가 위로 끝까지 올라올때까지 반복
    while seokhwan.cur_location()[0] != 0:
        # 계속 걸어라
        seokhwan.walk()

    print("#{} {}".format(tc, seokhwan.cur_location()[1] - 1))