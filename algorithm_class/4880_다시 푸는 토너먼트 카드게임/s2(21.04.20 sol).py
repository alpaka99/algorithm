import sys
sys.stdin = open('input.txt', 'r')

def rsp(students:list):
    n = len(students)
    if n == 1:
        return list(students)
    elif n == 2:
        first = students[0]
        second = students[1]

        # 서로 낸것
        first_rsp = first[1]
        second_rsp = second[1]

        # 2번이 이김
        if rsp_dict[first_rsp][0] == second_rsp:
            return [second]
        # 1번이 이김
        elif rsp_dict[first_rsp][1] == second_rsp:
            return [first]
        # 비김 = 1번이 이김
        else:
            return [first]
    else:
        left = rsp(students[:(n+1) // 2])
        right = rsp(students[(n+1) // 2:])

        return rsp(left+right)


for tc in range(1, int(input())+1):
    # 1은 가위, 2는 바위, 3은 보

    N = int(input())
    cards = list(map(int, input().split()))
    students = []
    # 학생 번호랑 가위바위보를 저장
    # (번호, 가위바위보)
    for i in range(len(cards)):
        students.append((i+1, cards[i]))


    # 내가 낸것:(상대가 이김, 상대가 짐)
    rsp_dict = {1:(2, 3), 2:(3, 1), 3:(1, 2)}

    ans = rsp(students)
    print("#{} {}".format(tc, ans[0][0]))
