import sys
sys.stdin = open('input.txt', 'r')

def dec2bin(num:int):
    ans = ''
    for i in range(4):
        if num & (1 << i):
            ans = '1' + ans
        else:
            ans = '0' + ans
    return ans



for tc in range(1, int(input())+1):
    answer = ''
    hex2dec_dict = {
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
    }

    N, hex = input().split()

    for letter in hex:
        if letter.isdigit():
            answer += dec2bin(int(letter))
        else:
            answer += dec2bin(hex2dec_dict[letter])
    print(answer)
