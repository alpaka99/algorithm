import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    tmp = list(input())
    M = []
    for i in range(len(tmp)):
        M.append(bool(int(tmp[i])))
    restore = [False]*len(M)


    count = 0
    pos = 0
    while pos < len(M):
        if M[pos] != restore[pos]:
            count += 1
            for i in range(pos,len(restore)):
                restore[i] = not(restore[i])
            #print(restore)
        pos += 1
    print("#{} {}".format(tc,count))