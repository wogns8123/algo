def f(i,k,R):
    if i == R:
        print(p)
    else:
        for j in range(k):
            if used[j]==0:
                used[j] = 1
                p[i] = a[j]
                f(i+1,k,R)
                used[j] = 0
N = 6
R= 6
a = [1,2,4,7,8,3]
p = [0] *R
used = [0] * N
f(0,N,R)
