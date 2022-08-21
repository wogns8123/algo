tc = int(input())
for test in range(tc):
    arr = list(map(int,input().split()))
    n = len(arr)
    result = []
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(j)
        result.append(subset)
    count = 0
    for i in result:
        if sum(i) == 0:
            count = 1
        else:
            count = 0
    print(f'#{test+1} {count}')
