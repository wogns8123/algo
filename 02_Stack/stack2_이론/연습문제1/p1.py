tc = int(input())
for test in range(tc):
    s = input()
    result = []
    stack = []
    for i in s:
        if i.isdigit():         # i가 숫자이면 result에 저장
            result.append(i)
        elif i=='+' or i=='-' or i=='*' or i=='/':  # i가 연산자이면 stack에 저장
            stack.append(i)
    for _ in range(len(stack)):
        result+= stack.pop()
    print(f'#{test+1}', end=' ')
    print(''.join(result))