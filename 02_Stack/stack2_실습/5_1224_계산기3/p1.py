import sys
sys.stdin = open('input.txt')
# 중위 -> 후위
def infix_(s):
    result = []
    stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2,'(' : 0,')':0}

    for i in s:
        if i.isdigit():
            result.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i =='*' or i == '+' or i == '/' or i=='/':
                while stack and priority[i]<=priority[stack[-1]]:
                    result.append(stack.pop())
                stack.append(i)
            elif i ==')':
                while result[-1] != '(':
                    result.append(stack.pop())
    while stack:
        result.append(stack.pop())
    return result

for test in range(10):
    num = int(input())
    s = input()
    post = infix_(s)        # post = 후위계산식
    cal = []
    for i in post:
        if i.isdigit():
            cal.append(int(i))
        elif i == '+':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1+num2)
        elif i == '-':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1-num2)
        elif i == '*':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1*num2)
        elif i == '/':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1/num2)
    print(f'#{test+1}',end=' ')
    print(*cal)

