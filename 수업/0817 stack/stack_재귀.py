def f(i,N):         # i 현재 단계 N 목표단계
    if i == N:
        return
    else:
        print(i)
        f(i+1,N)
f(0,999)