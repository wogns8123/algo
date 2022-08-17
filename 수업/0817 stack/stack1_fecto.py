def facto(N):
    if N == 1:
        return 1
    else:
        return facto(N-1) * N

for i in range(1,21):
    print(facto(i))