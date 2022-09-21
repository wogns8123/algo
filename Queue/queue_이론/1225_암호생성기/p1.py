import sys
sys.stdin = open('input (1).txt')

for test in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))        # 큐 형식

    while True:
        for i in range(1,6):            # 사이클
            number = arr.pop(0)         # 가장 앞의 요소 빼고
            arr.append(number-i)        # 사이클이 돌때마다 감소하는 숫자 변경
            if arr[-1] <= 0:            # 마지막이 0보다 작아지면 break
                arr[-1] = 0
                break
        if arr[-1] <= 0:                # while문 break
            break
    print(f'#{test}', end=' ')
    print(*arr)


