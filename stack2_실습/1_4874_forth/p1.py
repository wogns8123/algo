import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    s = list(map(str,input().split()))
    cal = 0
    stack = []
    error = False
    try:

        for i in s:
            if i.isdigit():
                stack.append(int(i))
            elif i == '+':
                number = stack.pop()
                stack.append(stack.pop() + number)
            elif i == '-':
                number = stack.pop()
                stack.append(stack.pop()-number)
            elif i == '*':
                number = stack.pop()
                stack.append(stack.pop()*number)
            elif i == '/':
                number = stack.pop()
                stack.append(stack.pop()//number)
            else:           # 결과까지 pop했는데 stack에 남아있을 경우 error
                cal = stack.pop()
                if len(stack) != 0:
                    error = True
                break
    except:     # i가 연산자일 때 stack에 수 2개가 없을 경우 빈리스트 pop에러
        error = True
    if error:
        print(f'#{test + 1} error')
    else:
        print(f'#{test+1} {cal}')


