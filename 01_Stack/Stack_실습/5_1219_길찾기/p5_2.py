import sys
sys.stdin=open('input.txt')
for _ in range(10):
    tc, n = map(int, input().split())

    # 경로를 딕셔너리로 저장
    # {1:[2,3], 2:[4,8]}
    adj_list = list(map(int, input().split()))
    graph = {x: [] for x in range(100)}
    for i in range(0, n * 2, 2):
        start= adj_list[i]
        end = adj_list[i + 1]
        graph[start].append(end)

    stack = [0]
    # 중복탐색을 막기 위해 visit을 활용
    visit = [0] * (100)
    visit[0] = 1

    result = 0
    while stack:
        c = stack.pop()
        for neighbor in graph[c]:
            # 끝점을 만나면 길이 있다는 의미이므로 1을 담아주고 while문을 끝내준다.
            if neighbor == 99:
                result = 1
                break
            if visit[neighbor] == 0:
                stack.append(neighbor)
                visit[neighbor] = 1

    print(f'#{tc} {result}')