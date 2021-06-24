# reversed() 직접 구현

def reverse_str(word):
    """
    word를 뒤집어 반환 - 반복문
    """
    # return 할 빈 string ans
    ans = ''
    # index를 끝에서 부터 접근하여 ans에 concatinate
    for i in range(len(word)-1, -1, -1):
        ans += word[i]
    return ans

word = 'tomato'
print(reverse_str(word))