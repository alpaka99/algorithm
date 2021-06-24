def solution(n, k, command):
    # 처음 표의 행 개수를 나타내는 정수 n,
    # 처음에 선택된 행의 위치를 나타내는 정수 k,
    # 수행한 명령어들이 담긴 문자열 배열 cmd

    answer = ''
    name = [i for i in range(n)]
    alive = ['O' for _ in range(n)]
    stack = []
    for cmd in command:
        if len(cmd) >= 2:
            com, val = cmd[0], cmd[2]
        else:
            com = cmd

        # 아래로
        if com == 'D':
            k += int(val)
        # 위로
        elif com == 'U':
            k -= int(val)
        # 삭제
        elif com == 'C':
            tmp = name.pop(k)
            stack.append(tmp)
            alive[tmp] = 'X'
            if k >= len(name):
                k = len(name)-1
        # 되돌리기
        elif com == 'Z':
            tmp = stack.pop()
            if tmp >= k:
                name.insert(tmp, tmp)
                alive[tmp] = 'O'
            else:
                name.insert(tmp, tmp)
                alive[tmp] = 'O'
                k += 1

    # for elem in alive:
    #     answer += elem
    answer = ''.join(alive)
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))