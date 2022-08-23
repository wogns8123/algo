import sys
sys.stdin=open('input.txt')

for test in range(10):
    num = int(input())
    s = input()
    stack = []
    result = []
    for i in s:
        if i.isdigit():
            result.append(i)
        elif not stack and i == '+':
            stack.append(i)
        elif stack and i == '+':
            result+=stack.pop()
            stack.append(i)

    # 여기까지 후위계산식 생성
    # 후위계산식 result
    result2= []
    for i in result:
        if i.isdigit():
            result2.append(int(i))
        elif i == '+':
            num_1 = result2.pop()
            num_2 = result2.pop()
            result2.append(num_1+num_2)
        result2.append(int(result2.pop()))
    print(f'#{test+1} {sum(result2)}')



