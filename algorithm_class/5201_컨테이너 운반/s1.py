import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int, input().split())

    package = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    package.sort(reverse=True)
    truck.sort(reverse=True)


    # 총 적재한 무게
    total = 0
    truck_pos = 0
    package_pos = 0
    while package_pos < len(package):
        i = 0
        while truck_pos + i < len(truck):
            if package[package_pos] <= truck[truck_pos+i]:
                total += package[package_pos]
                package_pos += 1
                truck_pos += i
                break
            i += 1

    print(total)