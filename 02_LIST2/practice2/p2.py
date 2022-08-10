tc = int(input())

for test in range(tc):
    arr = list(map(int,input().split()))
    n = len(arr)

    for i in range(1, 1<<n):
        result = 0
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += arr[j]
        if sum == 0:
            result += 1
            break
    print(f'#{test+1} {result}')



