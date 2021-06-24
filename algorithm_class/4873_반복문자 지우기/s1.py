import sys
sys.stdin  = open('input.txt', 'r', encoding='utf8')
def isEmpty(stack):
    if len(stack):
        return 0
    return 1


for tc in range(1, int(input())+1):
    letters = input()

    ans = 0

    stack = []

    for i in range(len(letters)):
        # 비어있으면 무조건 하나를 넣어줌
        if isEmpty(stack):
            stack.append(letters[i])
        # 비어있지 않으면 중복 검사
        else:
            if stack[-1] == letters[i]:
                ans += 1
                stack.pop()
            else:
                stack.append(letters[i])

    print("#{} {}".format(tc, len(stack)))