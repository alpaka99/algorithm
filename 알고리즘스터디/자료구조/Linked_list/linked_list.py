# 링크드 리스트 자체를 객체로 만들어야함
# https://daimhada.tistory.com/99?category=820522
class Dlist:
    # 양방향 링크드 리스트는 모든 Node의 시작인 head와
    # 모든 Node의 끝인 tail이 있어야 함
    def __init__(self):
        self.head = None
        self.tail = None

    # Node정의
    class Node:
        def __init__(self,data, p=None, n=None):
            self.data = data
            self.prev = p
            self.next = n

    # 맨앞에 노드 추가
    def add_first(self,data):
        # Dlist의 head가 비었다??
        # 아무런 노드가 없다는 뜻
        # 따라서 새로운 node를 생성하여 그 앞에 head, 그 뒤에 tail을 연결
        if self.head == None:
            self.head = self.Node(data)
            self.tail = self.head
        # 어떤 노드가 이미 있을떄 add
        else:
            self.head = self.Node(data,
                                  p=self.head,
                                  n=self.head.next.prev)
    # 맨뒤에 노드 추가
    def add_last(self,data):
        if self.tail == None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.tail = self.Node(data,
                                  p=self.tail.prev.next,
                                  n=self.tail)

    def delete_node(self, data):
        self.cur = self.head
        while self.cur.data != data:
            self.cur = self.cur.next
        # 도착
        self.cur.prev.next = self.cur.next.prev
        self.cur.next.prev = self.cur.prev.next
        self.cur.delete()


