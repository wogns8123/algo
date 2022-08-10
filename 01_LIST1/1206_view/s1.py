for test in range(10):
    num = int(input())
    arr = list(map(int,input().split()))
    count = 0

    for i in range(2,num-2):
        left = arr[i-2]
        if arr[i-1] > left:
            left = arr[i-1]

        right = arr[i+2]
        if arr[i+1] > right:
            right = arr[i+1]

        if arr[i]> left and arr[i] > right:
            a = arr[i] - left
            b = arr[i] - right
            if b < a:
                a = b
            count += a
    print(f'#{test+1} {count}')

