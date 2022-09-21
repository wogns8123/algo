tc = int(input())
for test in range(tc):
    num = int(input())
    arr = list(map(int, input().split()))

    max = 0
    for i in range(num):
        count = 0
        for j in range(i + 1, num):
            # 첫번째를 가장 높다고 가정
            if arr[i] > arr[j]:
                count += 1
        if max < count:
            max = count
    print(f'#{test + 1} {max}')
