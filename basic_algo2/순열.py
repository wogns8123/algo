def f(i,k):
    if i ==k:
        print(p)
    else:
        for j in range(1,k):
            p[i],p[j] = p[j],p[i]
            f(i+1,k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3,4,5,6]
f(0,6)