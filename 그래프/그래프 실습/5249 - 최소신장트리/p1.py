import sys
sys.stdin = open('input.txt')

def Find_Set(x):
    if x == p[x]:
        return x
    else:
        return Find_Set(p[x])

def Union(x,y):
    p[Find_Set(y)] = Find_Set(x)

tc = int(input())
for test in range(tc):
    V, E =map(int,input().split())
    E_list = []
    total = 0
    p = [0] *(V+1)
    for i in range(1,V+1):
        p[i] = i

    for _ in range(E):
        n1,n2,w = map(int,input().split())
        E_list.append((n1,n2,w))
    E_list.sort(key = lambda x : x[2])
    for i in range(E):
        n1,n2,w = E_list[i]
        if Find_Set(n1) != Find_Set(n2):
            Union(n1,n2)
            total += w
    print(f'#{test+1} {total}')