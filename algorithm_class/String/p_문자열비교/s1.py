
def str_comparision(str1, str2):
    """
    문자열이 같은지 비교해서
    같으면 True 반환
    같지 않으면 False 반환
    """
    try:
        for i in range(str1):
            if str1[i] != str2[i]:
                return False
        return True
    except:
        return False
str1 = 'abccd'
str2 = 'abcd'

print(str_comparision(str1, str2))