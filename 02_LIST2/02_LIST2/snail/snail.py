tc= int(input())
for test in range(tc):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    ''' N = 4
    [0, 0] 0 0 [0, N-1] [start, start] / [start, end] 
    0 0 0 0
    0 0 0 0
    [N-1, 0] 0 0 [N-1,N-1] [end, start] / [end, end]
    '''
    start = 0
    end = n - 1
    number = 1

    while n>0:
        # [0,x]행 숫자 입력
        for i in range(start, end + 1):
            arr[start][i] = number
            number += 1
        # [3,x]행 숫자 입력
        for i in range(start + 1, end+1):  # range(1,5)
            arr[i][end] = number
            number += 1
        # [x,3]행 역순
        for i in range(end-1, start - 1, -1): # range(3, -1, -1)
            arr[end][i] = number
            number += 1
        # [0,x]행 역순 숫자
        for i in range(end - 1, start, -1): # range(3, 0, -1)
            arr[i][start] = number
            number += 1
        n -= 2
        start += 1
        end -=1

    print(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='')
        print()


