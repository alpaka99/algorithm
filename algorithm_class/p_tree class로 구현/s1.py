class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.val:
            # 왼쪽 자식이 없을때
            if self.left == None:
                self.left = Node(value)
            else:
                # 오른쪽 자식이 없을때
                if self.right == None:
                    self.right = Node(value)
                # 둘 다 있을때
                else:
                    # 더 낮은쪽으로 가서 node를 생성
                    left_height = self.check_height()
                    right_height = self.check_height()

                    if left_height <= right_height:
                        self.left.insert(value)
                    else:
                        self.right.insert(value)
        else:
            self.val = value


    def check_height(self):
        if self.left or self.right:
            if self.left:
                return self.left.check_height()+1
            elif self.right:
                return self.right.check_height()+1
        else:
            return 1

    # in order 방식의 traveling
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val, end=' ')
        v = self.val
        if self.right:
            self.right.PrintTree()



root = Node(1)
# root.insert(1)
# root.insert(2)
# root.insert(3)
for i in range(2, 14):
    root.insert(i)

root.PrintTree()