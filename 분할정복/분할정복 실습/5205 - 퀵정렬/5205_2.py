def partition(l,r):
    pivot = A[l]
    i,j = l,r
    while i<=j:
        while i<=j and A[i] <=pivot:
            i+= 1
        while i<=j and A[j] >= pivot:
            j -=1
        if i<j:
            A[i],A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def qsort(l,r):
    if l<r:
        s = partition(l,r)
        qsort(l,s-1)
        qsort(s+1,r)

tc = int(input())
for test in range(tc):
    N = int(input())
    A = list(map(int,input().split()))
    qsort(0,N-1)
    print(f'#{test+1} {A[N//2]}')

    # print(f'#{test+1} {ans[N//2]}')