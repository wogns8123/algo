N = 3
q = [0] * N
front = 0
rear = 0

rear=(rear+1)%N             # enqueue(10)
q[rear] = 10
rear=(rear+1)%N             # enqueue(10)
q[rear] = 20
rear=(rear+1)%N             # enqueue(10)
q[rear] = 30
rear=(rear+1)%N             # enqueue(10)
q[rear] = 40
# rear=(rear+1)%N             # enqueue(10)
# q[rear] = 50

print(q)
front = (front+1)%N          # dequeue()
print(q[front])
front = (front+1)%N          # dequeue()
print(q[front])
front = (front+1)%N          # dequeue()
print(q[front])

print(q)