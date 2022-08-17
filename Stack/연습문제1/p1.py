def push(N):
    stack.append(N)
def pop():
    stack.pop()

N = 10
stack = [0] * N
top = -1

top+=1
print(push(1))
top+=1
print(push(2))
top+=1
print(push(3))


print(pop())
print(pop())
print(pop())