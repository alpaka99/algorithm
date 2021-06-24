# itoa (Integer to ASCII)
# 숫자 -> 문자 / Python의 str()

def itoa(my_num):
    """
    인자로 받은 정수 my_num을 문자로 반환
    """
    # 반환할 값 my_str을 비어있는 string으로 초기화
    my_str = ''
    
    # my_num이 한자리수가 될때까지 반복
    while my_num > 9:
        # 가장 앞 부분을 string으로 만들어서 my_str과 concatinate
        my_str += str(my_num // 10)
        # 가장 앞부분을 제외한 나머지 부분을 저장해줌
        my_num %= 10
    # 마지막으로 남은 끝을 string으로 변환해서 넣어줌
    my_str += str(my_num)
    return my_str

my_num = 123
print(my_num, type(my_num))

my_str1 = itoa(my_num)
print(my_str1, type(my_str1))

my_str2 = str(my_num)
print(my_str2, type(my_str2))