import sys
sys.stdin=open('sample_input.txt')

def bfs(start,end,arr):
    visited = [0]*(len(arr)+1)  # 간 곳 체크하기위해
    q = []                      #
    visited[start] = 1          # 시작점 visited에 추가
    q.append(start)             # q
    while q:
        v = q.pop(0)

        # if v == end:
        #     return visited[start]
        if v == end:            # v가 end를 만나면 visitev[v]를 출력, visited이 1부터 시작하기때문에 1감소
            return visited[v]-1
        for i in arr[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v]+1
    return 0

tc = int(input())
for test in range(tc):
    V,E = map(int,input().split())
    # 리스트만들기
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)

    start, end = map(int,input().split())


    print(f'#{test+1} {bfs(start,end,arr)}')