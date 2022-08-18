def push(N):
    stack.append(N)
def pop():
    stack.pop()

N = 10
stack = [0] * N
top = -1

top+=1
push(1)
print(stack)
top+=1
push(2)
print(stack)
top+=1
push(3)
print(stack)

top = pop()
print(stack)
top = pop()
print(stack)
top = pop()
print(stack)