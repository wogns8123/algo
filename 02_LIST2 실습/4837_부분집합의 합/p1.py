import sys
sys.stdin = open('sample_input (1).txt')

tc = int(input())

for test in range(tc):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    result = []
    count = 0

    for i in range(1 << len(arr)):
        arr_list = []
        for j in range(len(arr)):
            if i & (1 << j):
                arr_list.append(arr[j])
        result.append(arr_list)

    for i in result:
        if sum(i) == K and len(i) == N:
            count += 1
    print(f'#{test + 1} {count}')
