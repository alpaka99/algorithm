import sys
sys.stdin = open('input2.txt', 'r')

for tc in range(1, int(input())+1):
    command = input().split()
    answers = []
    for i in range(len(command)):
        if not (command[i] in answers):
            print(0)