def isEmpty():
    return len(queue)==0
def enQueue(item):  #원형큐의 삽입연산
    queue.append(item)
def deQueue():      #원형 큐의 삭제 연산
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue.pop(0)
def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue[0]

queue = []
front = -1
rear = len(queue)-1
enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())