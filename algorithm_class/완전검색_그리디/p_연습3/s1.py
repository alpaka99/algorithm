"""
연습 문제3. 2의 거듭제곱

2의 거듭 제곱을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복
def power_of_two_iteration(k):
    answer = 1
    for _ in range(4):
        answer *= 2
    return answer

print(power_of_two_iteration(4))


# 재귀
def power_of_two_recursion(k):
    if k == 0:
        return 1

    return power_of_two_recursion(k-1)*2

print(power_of_two_recursion(4))