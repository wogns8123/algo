import sys

sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    s = input()
    stack = []
    top = -1
    result = 0
    for i in s:
        if i == '{' or i == '(':        # 여는문자 append
            top += 1                    # top끌고감
            stack.append(i)
        elif i == '}' or i == ')':      # 닫는문자나오면
            if not stack:               # 스택이 비었는지 확인하고
                print(f'#{test + 1} 0')
                break # 비었으면 멈추기
            elif i == ')' and stack.pop() != '(':
                print(f'#{test + 1} 0')

            elif i == '}' and stack.pop() != '{':
                print(f'#{test + 1} 0')

    if stack:
        print(f'#{test + 1} 0')
    else:
        print(f'#{test + 1} 1')



