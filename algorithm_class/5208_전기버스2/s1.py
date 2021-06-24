import sys
sys.stdin = open('input.txt', 'r')
global min_val

def powerset(bus_stop:list, N:int):
    arr = {}
    for i in range(1<<N-1):
        tmp = []
        for j in range(N):
            if i &(1<<j):
                tmp.append(bus_stop[j])
        n = len(tmp)
        if arr.get(n):
            arr[n] += [tmp]
        else:
            arr[n] = [tmp]
    return arr
        # global min_val
        # if n < min_val:
        #     ans = can_reach(tmp,N)
        #     if ans:
        #         min_val = n


def can_reach(arr:list,N:int):
    if sum(arr) >= N:
        return True
    else:
        return False

for tc in range(1, int(input())+1):
    data = list(map(int, input().split()))
    N = data[0]
    bus_stop = data[1:]
    min_val = 100*N
    possible_dict = powerset(bus_stop,N)

    # print(possibilities.items())
    # values = possibilities.values()
    reach_flag = False
    for i in range(2,1<<N):
        cur_val =possible_dict[i]
        for item in cur_val:
            reach_flag = can_reach(item,N)
            if reach_flag:
                min_val = i
                break
        if reach_flag:
            break

    print("#{} {}".format(tc,min_val-1))