class Queue:
    def __init__(self,n):
        self.size = n
        self.items = [None] * n
        self.front = -1
        self.rear = -1
    def enQueue(self,item):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.items[self.rear] = item
    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.front += 1
            self.items[self.front]
            self.items[self.front] = None
            return self.items
    def isEmpty(self):
        # if self.front == self.rear:
        #     return True
        # else:
        #     return False
        return self.rear == self.front      # 위의 4줄을 한 줄로
    def isFull(self):
        if self.rear == self.size -1:
            return True
        else:
            return False
    def Qppek(self):
        return self.items[self.front]

Q = Queue(3)
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
print(Q.items)
print(Q.deQueue())
print(Q.items)
print(Q.deQueue())
print(Q.items)
print(Q.deQueue())
print(Q.items)
