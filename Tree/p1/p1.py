def preorder(n):
    if n:
        preorder(ch1[n])
        print(n, end=' ')
        preorder(ch2[n])

E = int(input())
V = E +1
arr = list(map(int,input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(V-1):
    p,c = arr[2*i], arr[2*i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
preorder(1)


'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''