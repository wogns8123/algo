
tc = int(input())
for test in range(tc):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))

    idx = b%a
    print(f'#{test+1} {arr[idx]}')
