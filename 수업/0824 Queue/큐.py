N = 10
q = [0] * N
front = -1
rear = -1

rear+=1             # enqueue(10)
q[rear] = 10
rear+=1             # enqueue(20)
q[rear] = 20
rear+=1             # enqueue(30)
q[rear] = 30
rear+=1             # enqueue(40)
q[rear] = 40
rear+=1             # enqueue(50)
q[rear] = 50

front += 1          # dequeue()
print(q[front])
front += 1          # dequeue()
print(q[front])
front += 1          # dequeue()
print(q[front])