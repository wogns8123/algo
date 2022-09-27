import sys
sys.stdin = open('input.txt')

def f(i,k):
    global ans
    if i==k:
        for w in range(len(p_list)):
            total = 0
            min_idx = 9999
            for q in range(N):
                total += arr[q][p_list[q]-1]
                if min_idx>total :
                    min_idx = total
            ans.append(total)
    else:
        for j in range(i,k):
            p_list[i],p_list[j] = p_list[j],p_list[i]
            f(i+1,k)
            p_list[i], p_list[j] = p_list[j], p_list[i]



tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    dp = [[0] * N for _ in range(N)]
    p_list = [i for i in range(1,N+1)]
    # for i in range(N):
    #     arr[i][]
    f(0,N)
    print(f'#{test+1} {min(ans)}')
