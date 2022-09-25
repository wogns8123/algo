a = [1,2,3,4,5,6]
r = 3
p = [0] * r
used = [0] * len(a)

def f(i,k,r):
    if i ==r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1,k,r)
                used[j] = 0
f(0,len(a),r)

