# atoi (ASCII to Integer)
# 문자 -> 숫자 / Python의 int()

def atoi(my_str):
    """
    인자로 받은 정수 my_num을 문자로 반환
    """
    # retrun 해줄 값 0으로 초기화
    my_num = 0

    # for문으로 마지막 글자를 제외하고 한글자 한글자 순회함
    for i in range(len(my_str)-1):
        my_num += int(my_str[i])
        my_num *= 10
    # 마지막 글자 넣어줌
    my_num += int(my_str[len(my_str)-1])
    return my_num

my_str = '123'
print(my_str, type(my_str))

my_int1 = atoi(my_str)
print(my_int1, type(my_int1))

my_int2 = int(my_str)
print(my_int2, type(my_int2))