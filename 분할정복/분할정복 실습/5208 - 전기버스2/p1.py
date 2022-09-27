import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    N, *arr = map(int,input().split())
    dp = [-1]*N
    for i in range(len(arr)):
        for j in range(1,arr[i]+1):    # 배터리마다 순회
            if dp[i+j] == -1:
                dp[i+j] = dp[i]+1
            if i+j >= N-1:
                break
        else:
            continue
        break

    print(f'#{test+1} {dp[N-1]}')