import sys

sys.stdin = open('sample_input.txt')
tc = int(input())
for test in range(tc):
    s = input()
    stack = []
    top = -1
    result = 0
    for i in s:
        if i =='{' or i == '(':
            top += 1
            stack.append(i)
        if i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                break
        if i == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    break
            else:
                break
    else:
        if not stack:
            result = 1

    print(f'#{test + 1} {result}')
