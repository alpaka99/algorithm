import sys
sys.stdin = open('input.txt', 'r')

def make_bin_set(bin:list):
    for i in range(len(bin)):
        tmp = bin[:]
        if bin[i] == '1':
            tmp[i] = '0'

        else:
            tmp[i] = '1'
        bin_set.add(''.join(tmp))


def bin2dec(bin_set:set):
    while bin_set:
        bin = bin_set.pop()
        tmp = 0
        N = len(bin)
        for i in range(N):
            tmp += 2**(N-i-1)*int(bin[i])
        num_set.add(tmp)


def make_tri_set(tri:list):
    for i in range(len(tri)):
        tmp = tri[:]
        if tri[i] != '0':
            tmp[i] = '0'
            tri_set.add(''.join(tmp))
        if tri[i] != '1':
            tmp[i] = '1'
            tri_set.add(''.join(tmp))
        if tri[i] != '2':
            tmp[i] = '2'
            tri_set.add(''.join(tmp))

def tri2dec(tri_set:set):
    while tri_set:
        tri = tri_set.pop()
        tmp = 0
        N = len(tri)
        for i in range(N):
            tmp += 3**(N-i-1)*int(tri[i])

        if tmp in num_set:
            return tmp
        # tri_num_set.add(tmp)



for tc in range(1, int(input())+1):
    bin = list(input())
    tri = list(input())

    bin_set = set()
    tri_set = set()
    num_set = set()
    tri_num_set = set()

    make_bin_set(bin)
    make_tri_set(tri)


    bin2dec(bin_set)
    ans = tri2dec(tri_set)
    print("#{} {}".format(tc,ans))
