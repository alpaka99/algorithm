"""
연습 문제2. 선택 정렬 (반복 & 재귀)

선택 정렬을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복(for)
def selection_sort_for(my_list:list):
    for i in range(len(my_list)-1):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]


# 재귀 - 추가 파라미터 구성 가능
def selection_sort_recursion(my_list:list):
    # 탈출 조건
    if len(my_list) == 1:
        return my_list

    pass




selection_sort_for(my_list)
print(my_list)

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

