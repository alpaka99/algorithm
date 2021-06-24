# reversed() 직접 구현

def reverse_str_recursion(word):
    """
    word를 뒤집어 반환 - 재귀함수
    """
    # 재귀함수의 포인트인 종료조건
    if len(word) <= 1:
        # 이 경우 원래 word의 가장 마지막 글자가 return 됨
        return word
    
    # 종료조건에 걸리지 않았으면 더 내려가야함
    # 이 전에 word가 뒤집힌게 return되어 올 것이므로 현재 가장 앞글자를 가장 뒤에 붙혀줌
    remain_word = ''
    for i in range(1, len(word)):
        remain_word += word[i]
    return reverse_str_recursion(remain_word) + word[0]
word = 'tomato'
print(reverse_str_recursion(word))