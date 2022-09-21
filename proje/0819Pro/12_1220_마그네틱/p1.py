import sys
sys.stdin = open('input.txt')

# 1 = N극
# 2 = S극
for test in range(10):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))

    stack = []
    top = -1
    for i in arr2:
        for j in i:
            if j == '1':
                top += 1
                stack.append(j)
            elif j == '2':
                top += 1
                stack.append(j)

    print(stack)
    # 가장 위가 2이거나 가장 아래가 1일 경우
    while True:
        for i in stack:
            if stack[0] == '2':
                stack.pop(0)
            elif stack[-1] == '1':
                stack.pop(-1)
        else:
            break
    print(len(stack))
    count = 0
    for i in range(len(stack) - 1):
        if stack[i] == '1' and stack[i + 1] == '2':
            count += 1
    print(count)
