import sys
sys.stdin=open('input.txt')
T = int(input())

for t in range(T):
    stack = []
    nums = []
    li = list(input())
    for i in li:
        if i == '(':
            stack.append(i)
        elif  i == '+' or i == '-':
            try:
                if len(stack) != 0:
                    while stack[-1] == '*' or  stack[-1] == '/' or stack[-1] == '-' or  stack[-1] == '+':
                        nums.append(stack.pop())
                stack.append(i)
            except IndexError:
                continue
        elif i == '/' or i == '*':
            if len(stack) != 0:
                while stack[-1] == '*' or  stack[-1] == '/':
                    nums.append(stack.pop())
            stack.append(i)
        elif i == ")":
            while stack[-1] != '(':
                nums.append(stack.pop())
            stack.pop()
        else:
            nums.append(int(i))
    stack = stack[::-1]
    print(f'#{t+1} ',end='')
    print(*nums,*stack,sep="")