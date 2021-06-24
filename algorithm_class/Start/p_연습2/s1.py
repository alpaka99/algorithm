"""
연습 문제 2. 음수 표현
이진수에서 음수 표현에 대해 간단하게 정리해보세요!
- 참고 자료: https://ko.wikipedia.org/wiki/2%EC%9D%98_%EB%B3%B4%EC%88%98

1. 2의 보수 ?
- 개념과 예시
2의 보수(--補數, 영어: two's complement)란
어떤 수를 커다란 2의 제곱수에서 빼서 얻은 이진수이다

예를 들면 10101의 보수는
1) 10101보다 큰 수인 100000에서 10101을 뺀 1011이다.

ex)

100000
-10101
------
001011

혹은
1) 주어진 이진수의 모든 자리의 숫자를 반전(0을 1로, 1을 0으로)시킨 뒤
2) 여기에 1을 더하면 2의 보수를 얻을 수 있다.

ex)

10101 -> 01010
01010


2. 이진수에서 뺄셈 ?
- 개념과 예시

"""