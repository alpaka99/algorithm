import sys
# sys.stdin = open('input.txt')
sys.stdin = open("input.txt", "r")

n = int(input())
print(n%2)

numbers = map(int,input().split())
result = 0
for number in numbers:
    result += number
print(result)

N = int(input())
box = []
for _ in range(N):
    box.append(input().split())

print(box[1][1])