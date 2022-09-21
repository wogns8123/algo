import sys

sys.stdin = open('input.txt')

# 1 = N극
# 2 = S극
for test in range(10):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))

    stack = []
    top = -1
    for i in arr2:
        line = []
        for j in i:
            if j == '1':
                top += 1
                line.append(j)
            elif j == '2':
                top += 1
                line.append(j)
        stack.append(line)

    # 가장 위가 2이거나 가장 아래가 1일 경우
    while True:
        for i in stack:
            for j in range(len(i)):
                if i[0] == '2':
                    i.pop(0)
                elif i[-1] == '1':
                    i.pop(-1)
        else:
            break
    count = 0
    for i in stack:
        for j in range(len(i)):
            if i[j] == '1' and i[j + 1] == '2':
                count += 1
    print(f'#{test+1} {count}')
