import sys
sys.stdin=open('input.txt')

def BFS(n,target):
    global result
    que = []
    que.append(n)
    while que:
        node = que.pop(0)
        if node == target:

            break
        else:
            lst = [node + 1, node-1,node*2,node-10]
            for i in lst:
                if 0<= i <= 1000000:
                    if visited[i] ==0:
                        visited[i] = visited[node] + 1
                        que.append(i)
    return visited


tc =int(input())
for test in range(tc):
    N, M = map(int,input().split())
    result = 0
    visited = [0] * 100
    print(BFS(N,M))