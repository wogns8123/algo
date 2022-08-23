import sys
sys.stdin = open('input.txt')
for T in range(10):
    N = int(input())
    infix = input()
    stack = []
    postfix = ''
    stack2 = []

    for x in infix:
        if ord('0') <= ord(x) <= ord('9'):
            postfix += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    postfix += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()

    while stack:
        postfix += stack.pop()

print(postfix)