import sys
sys.stdin = open('input.txt', 'r')

def check_babygin(cnt_list:list):
    # triplet 검사
    for i in range(10):
        if cnt_list[i]:
            if i+1 < 10 and i+2 < 10:
                if cnt_list[i+1] and cnt_list[i+2]:
                    return True

                elif cnt_list[i] // 3 >= 1:
                    return True
    return False

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    person_1 = [ 0 for _ in range(10)]
    person_2 = [ 0 for _ in range(10)]

    i = 0
    flag_1 = False
    flag_2 = False
    while i < len(cards):
        person_1[cards[i]] += 1
        flag_1 = check_babygin(person_1)
        person_2[cards[i+1]] += 1
        flag_2 = check_babygin(person_2)

        if flag_1:
            print("#{} {}".format(tc,1))
            break
        elif flag_2:
            print("#{} {}".format(tc,2))
            break
        else:
            flag_1, flag_2 = False, False
            i += 2
    if flag_1 or flag_2:
        pass
    else:
        print("#{} {}".format(tc,0))