import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    number = int(input())
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(f'#{test+1} ', end= '')
    print(*arr)