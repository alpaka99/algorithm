"""
연습 문제 4.

0과 1로 이루어진 1차원 배열에서 7bit 단위로 묶어 10진수로 출력하기
- arr는 편의상 분리한 것이기 때문에 연속된 수로 간주할 것

입력 예시)
0 0 0 0 0 0 1 0 0 0 1 1 0 1

0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 0 0 1 1 1

출력 예시)
1 13

0 120 12 7 76 24 60 121 124 103
"""

arr = [
       0,0,0,0,0,0,0, 1,1,1,1,0,0,0, 0,0,0,1,1,0,0, 0,0,0,0,1,1,1, 1,0,0,1,1,0,0,
       0,0,1,1,0,0,0, 0,1,1,1,1,0,0, 1,1,1,1,0,0,1, 1,1,1,1,1,0,0, 1,1,0,0,1,1,1
      ]

while arr:
    tmp = arr[:7]
    arr = arr[7:]

    num = 0


    #print(tmp)

    for i in range(7):
        num += tmp[i]*(2**(6-i))

    print(num, end=' ')
