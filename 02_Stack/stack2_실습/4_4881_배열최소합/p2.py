import sys
sys.stdin = open('sample_input.txt')
def perm(arr,n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n>1 :
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans,n-1):
                result.append([arr[i]]+p)
    return result

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    small_arr = list(range(n))
    print(perm(small_arr,n))

    for i in range(n):
        for j in range(n):
            print(perm(small_arr,n)[i][j])
            print(arr[j][perm(small_arr,n)[i][j]], end=' ')

    #
    #         print(arr[i][j])



