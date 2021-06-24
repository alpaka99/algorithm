"""
연습문제 4. 순열

4-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

my_list = [1, 2, 3]
permutations = []
for i in my_list:
    for j in my_list:
        if i != j:
            for k in my_list:
                if i != k and j != k:
                    permutations.append([i, j, k])

for permutation in permutations:
    print(*permutation)
