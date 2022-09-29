import sys
sys.stdin = open('sample_input.txt')


tc = int(input())
for test in range(tc):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    adj = [[_] for _ in range(N+1)]
    p = []
    start_list= []
    end_list = []
    for i in range(0,len(arr),2):
        start_list.append(arr[i])
        end_list.append(arr[i+1])

    for i in range(M):
        adj[start_list[i]] += [end_list[i]]
        adj[end_list[i]] += [start_list[i]]
        adj[end_list[i]].pop()
    print(adj)
    for i in adj:
        for j in adj:
            if i == j:
                i = []
    print(adj)



