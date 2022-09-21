import sys
sys.stdin=open('sample_input.txt')

def asd f(lst,n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in lst:
            result.append(i)
    elif n>1:
        for i in range(len(arr)):
            ans = [i for i in lst]
            ans.remove(lst[i])
            for p in asdf(ans,n-1):
                result.append(arr[i]+p)
    return result


tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    bit = [1] * N

    lst = list(range(0,N))
    print(asdf(lst,3))
