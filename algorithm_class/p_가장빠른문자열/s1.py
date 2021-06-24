"""
slicing을 끝 범위를 넘어가게 해도 해당 리스트의 끝까지만 본다
안전하다.(연욱님 아이디어)
"""
import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf-8')

for tc in range(1, int(input())+1):
    # 짧은거 긴거 나눠받기
    long_str ,short_str = input().split()
    # 몇번 타이핑을 하는지 저장하는 변수
    count = 0
    # 현재 타이핑할 위치를 저장하는 변수
    pos = 0
    # 타이핑 할 포지션이 범위를 벗어나지 않게끔
    while pos < len(long_str):
        # 지금 위치로부터 정해진 범위까지를 slicing했을떄
        # 한번에 치는 keyword가 있는지 확인
        if long_str[pos: pos+len(short_str)] == short_str:
            # 만약 같으면
            # 한번 쳤다는 뜻으로 count를 1 올려주고
            # keyword가 끝나는 지점까지 pos를 이동시켜줍니다.
            count += 1
            pos += len(short_str)
        else:
            # 같지 않을 경우 한 글자를 쳤다는 뜻으로 pos와 count를 1 증가시킴
            count += 1
            pos+=1
    print("#{} {}".format(tc,count))