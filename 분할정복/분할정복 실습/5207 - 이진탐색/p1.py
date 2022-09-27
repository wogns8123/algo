import sys
sys.stdin=open('input.txt')

def binary_search(arr,start, end, target):
    global ans

    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            ans.append(0)
            return mid
        elif arr[mid]>target:
            ans.append(1)
            return binary_search(arr,start,mid-1,target)

        elif arr[mid] < target:
            ans.append(2)
            return binary_search(arr,mid+1,end,target)


tc = int(input())
for test in range(tc):
    N,M = map(int,input().split())
    N_list = list(map(int,input().split()))
    M_list = list(map(int,input().split()))
    cnt = 0
    for i in range(len(M_list)):
        ans = []
        binary_search(N_list,0,len(N_list)-1,M_list[i])
        print(ans)

        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                cnt += 1


    print(N-cnt)


    print()