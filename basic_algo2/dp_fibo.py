def fibo(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]
    if n>=2 and len(memo)<=n:
        return n
    else:
        memo[n].append(fibo(n-1)+fibo(n-2))
    return memo[n]



memo = [0,1]


print(fibo(6))