tc = int(input())
for test in range(tc):
    s = input()
    stack = []
    top = -1
    for i in s:
        if i == '(':
            top += 1
            stack.append(1)
        elif i == ')':
            if stack:
                top -= 1
                stack.pop()
            else:
                print(f'#{test+1} -1')
                break
    else:
        if not stack:
            print(f'#{test+1} 1')
        else:
            print(f'#{test+1} -1')