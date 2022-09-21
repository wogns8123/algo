import sys
sys.stdin = open('sample_input (1).txt')

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = list(map(int,input().split()))
    arr_blank = [0]*N
    # 버블정렬
    # for i in range(N-1,0,-1):
    #     for j in range(0,i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    # 선택 정렬
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]

    for i in range(N):
        if i % 2 == 0:
            arr_blank[i] = arr[N - (i // 2)-1]
        elif i % 2 == 1:
            arr_blank[i] = arr[i // 2]
    result = arr_blank[:10]
    print(f'#{test+1}', end=' ')
    print(*result)
