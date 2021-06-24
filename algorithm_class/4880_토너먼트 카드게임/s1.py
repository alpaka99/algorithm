"""
앞 그룹과 뒷 그룹중 어느 그룹에 더 많은 사람이 들어가야하는지를 잘 안봐서
많이 틀렸다.
그리고 아직 재귀에 대한 숙련도가 부족하다
"""
import sys
sys.stdin = open('input.txt', 'r')

# 내 숫자: [나를 이김: 내가 이김]
# 1 가위, 2 바위, 3 보
rsp = {1:[2, 3], 2:[3, 1], 3:[1, 2]}

# divide & conquer형의 재귀 함수
def rock_scissors_paper(students: list):
    if len(students) == 1 : # 부전승
        return students.pop()
    else: # 나눠서 각각 넣어줌
        n = len(students)
        left = students[:(n+1)//2] # 앞 그룹에 더 많은 사람이 들어가야함
        right = students[(n+1)//2:] 
        return who_wins([rock_scissors_paper(left), rock_scissors_paper(right)])

def who_wins(students: list):
    # 튜플이 2개 들어있는 길이가 2인 리스트가 들어올거임
    student1, student2 = students

    #둘 중 누가 이겼나 판별
    if rsp[student1[1]][0] == student2[1]: # 2가 이김
        return student2
    elif rsp[student1[1]][1] == student2[1]: # 1이 이김
        return student1
    else:
        return student1 # 비겼을때는 더 작은 번호의 학생



for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    
    # 각 튜플의 [0]에는 학생의 번호, [1]에는 card의 번호 저장
    students = list(enumerate(cards))

    ans = rock_scissors_paper(students)
    print("#{} {}".format(tc,ans[0]+1))
