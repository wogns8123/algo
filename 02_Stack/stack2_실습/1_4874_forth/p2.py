import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    post = input()
    cal = []

    for i in post:
        if i.isdigit():
            cal.append(int(i))
        elif i == '+':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(int(num1)+int(num2))
        elif i == '*':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(int(num1)*int(num2))
    print(f'#{test+1}',end=' ')
    print(*cal)