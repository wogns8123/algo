def push(item, size):
    global top
    top += 1
    if top==size:
        print('overflow!')
    else:
        stack[top] = item
def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -=1
        return stack[top+1]
print(pop())

size = 10
stack = [0]*size
top = -1

push(10,size)
top += 1
stack[top] = 20

print(stack)