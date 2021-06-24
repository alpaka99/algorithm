# 원자 초기 좌표 x, y
# 움직임은 상(0)하(1)좌(2)우(3) 4방향뿐
# 이동속도는 1로 통일
# 동시에 이동
# 두개 이상의 원자가 충돌하면 모든 보유한 에너지를 방출하고 소멸
# 방출하는 에너지의 총합

import sys
sys.stdin = open('input.txt', 'r')



def simulate(atoms:dict):
    total_energy = 0

    # 상하좌우 방향벡터
    # 0:상 1:하 2:좌 3:우
    dr_dict = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}

    #matrix = [[ 0 for _ in range(2001)] for _ in range(2001)]

    # 흔적을 뜻하는 dict
    shadow = {}

    # 판에 원자들을 깔아 놨음
    atoms_key = list(atoms.keys())

    for i in range(len(atoms_key)):
        cur_atom = atoms.get(atoms_key[i])
        matrix[cur_atom[0]][cur_atom[1]] = atoms_key[i]
        shadow[i] = []


    while atoms:
        # 모든 원자들을 이동시킴
        atoms_key = list(atoms.keys())
        for i in range(len(atoms_key)):
            cur_atom = atoms.get(atoms_key[i])
            # shadow에 다 저장해놓고
            shadow[atoms_key[i]] = cur_atom[:]
            # atom은 움직임
            cur_r, cur_c = cur_atom[0], cur_atom[1]
            delta = dr_dict[cur_atom[2]]
            cur_r += delta[0]
            cur_c += delta[1]





for tc in range(1, int(input())+1):
    # 원자의 수
    N = int(input())


    # 만나는지 안만나는지는 어떻게?
    # 원자가 끝에 도달하면 탈출시키자!
    
    # 판에 남은 원자가 0이면 종료

    # 판에 원자들을 흩뿌려놓자
    matrix = [[0 for _ in range(2001)] for _ in range(2001)]


    atoms = {}
    # x위치, y위치 이동방향, 보유에너지 K
    for i in range(N):
        x, y, V, E = map(int, input().split())
        x += 1000
        y += 1000

        atoms[i] = [x, y, V, E] #움직일때마다 업데이트 해줘야함!



    simulate(atoms)