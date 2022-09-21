tc = int(input())

def m_sum(arr,M,idx):
    sum = 0
    for i in range(M):
        sum+=arr[i+idx]
    return sum

for tc_num in range(tc):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    sum_arr=[]

    for idx in range(N-(M-1)):
        sum_arr.append(m_sum(arr,M,idx))

    max_sum = 0
    min_sum = sum_arr[0]
    #최대값
    for idx in range(N-(M-1)):
        if max_sum < sum_arr[idx]:
            max_sum = sum_arr[idx]
    # 최소값
        if min_sum > sum_arr[idx]:
            min_sum = sum_arr[idx]
    print(f'#{tc_num+1} {max_sum-min_sum}')



