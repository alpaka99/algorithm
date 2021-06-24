import sys
sys.stdin = open('input.txt', 'r')

def check_parenthesis(line):
    sml_stack = []
    mid_stack = []

    # 0이면 소괄호가 마지막으로 들어감
    # 1이면 중괄호가 들어감

    sml_flag = False

    for i in range(len(line)):
        # 여는 괄호들은 다 push
        if line[i] == '(' or line[i] == '{':
            if line[i] == '(':
                sml_stack.append(line[i])
                sml_flag = True
            else:
                mid_stack.append(line[i])
                sml_flag = False
        else:
            # 닫는 괄호이면
            if line[i] == ')' or '}':
                pass




for tc in range(1, int(input())+1):
    line = input()

    # '(' = 40
    # ')' = 41
    # '{' = 123
    # '}' = 125
    # 124 = '|'
    print(check_parenthesis(line))