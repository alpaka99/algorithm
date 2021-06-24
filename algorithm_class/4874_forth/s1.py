"""
숨은 테케 찾는게 너무 어렵네요
try, except를 이용하여 풀었습니다
다은님, 대진님 아이디어: dict안에 value에 함수를 저장해서 연산자마다 맞는 함수를
호출하여 사용한다.
"""
import sys
sys.stdin = open('input.txt', 'r')

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return int(num1 / num2)

def calculate(string):
    # 연산자마다 해당하는 함수를 value로 저장해놓음 -> 새로 배운 포인트
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}


    i = 0
    stack = [] #연산하는 수를 저장하는 stack
    
    while i < len(string):
        if string[i].isdigit(): # 숫자면
            stack.append(int(string[i]))
        else: # 숫자가 아니면
            if string[i] == '.':
                if len(stack) == 1:
                    print("#{} {}".format(tc, stack.pop()))
                else:
                    # 이걸 생각 못해서 계속 틀렸음, 연산자가 다 끝났는데 연산이 안끝난 상황
                    print("#{} {}".format(tc, 'error')) 
            else:
                try: # try, except로 error 상황 찾아냄
                    num2 = stack.pop()
                    num1 = stack.pop()
                except:
                    print("#{} {}".format(tc, 'error'))
                    return
                
                # 대진님 다은님 아이디어 짱
                stack.append(op_dict[string[i]](num1,num2))

                ###### 이젠 이렇게 길게 안쓸거야 #########
                # if string[i] == '+':
                #     stack.append(int(num1 + num2))
                # elif string[i] == '-':
                #     stack.append(int(num1 - num2))
                # elif string[i] == '*':
                #     stack.append(int(num1 * num2))
                # elif string[i] == '/':
                #     stack.append(int(num1 / num2))

        i += 1


for tc in range(1, int(input())+1):
    string = input().split()

    calculate(string)