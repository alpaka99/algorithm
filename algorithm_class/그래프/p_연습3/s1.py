"""
연습 문제3. Queue 구현
 - 사이즈가 5인 고정 배열 Queue를 구현하시오.
"""
SIZE = 4
Q = [0] * SIZE

# 초기 상태의 표현 -> stack과 다르게 pointer가 2개
# front -> 삭제 위치(dequeue)
# rear -> 삽입 위치(enqueue)
front, rear = -1, -1
queue = [0]*SIZE

def is_full():
    """
    Queue가 포화상태인지 확인
    """
    if rear == SIZE:
        print('queue is full')
        return True
    return False

def is_empty():
    """
    Queue가 공백상태인지 확인
    """
    if front == rear:
        print('queue is empty')
        return True
    return False

def enqueue(n:int):
    """
    Queue의 뒤쪽(rear 다음)에 원소를 삽입
    - rear를 뒤쪽으로 옮기고(원소를 삽입 할 자리 마련) (rear + 1)그 자리에 원소를 삽입
    """
    global rear
    rear += 1

    if is_full():
        return


    queue[rear] = n



def dequeue():
    """
    Queue의 앞쪽(front)에서 원소를 삭제하고 반환
    - front를 뒤쪽으로 옮기고(front + 1) 그 자리에 있는 원소를 반환하며 삭제
    - 첫 번째 원소를 return -> 삭제와 동일한 기능
    """
    if is_empty():
        return
    global front
    front += 1
    return queue[front]

def Qpeek():
    """
    Queue의 앞쪽(front)의 한 자리뒤(front+1)에서 원소를 삭제없이 반환
    - front의 값을 단순하게 증가시켜 가져옴(큐의 첫 번째 원소 반환)
    """
    if is_empty():
        return
    return queue[front+1]

# is_empty
print(is_empty()) # True

# Queue 초기화
print(Q)
print('----------------')

# enQueue
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5) # Queue is full!

# Queue 확인
print(Q)
print('----------------')

# Qpeek
print(Qpeek()) # 1
print('----------------')

# is_empty
print(is_empty()) # False
print('----------------')

# deQueue
print(dequeue()) # 1
print(dequeue()) # 2
print(dequeue()) # 3
print(dequeue()) # 4
print(dequeue()) # Queue is empty!
print(Q)