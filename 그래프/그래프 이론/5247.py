from collections import deque
def BFS():
    global result
    while Q: #큐가 비어있지 않으면
        front, check = Q.popleft()
        if front == M:
            result = check
            return #함수 종료
        for i in range(4):
            if i == 0:
                if 1 <= front + 1 <= 1000000 and visited[front+1] == False:
                    Q.append((front+1, check+1))
                    visited[front+1] = True
            elif i == 1:
                if 1 <= front - 1 <= 1000000 and visited[front-1] == False:
                    Q.append((front-1, check+1))
                    visited[front - 1] = True
            elif i == 2:
                if 1 <= front * 2 <= 1000000 and visited[front*2] == False:
                    Q.append((front*2, check+1))
                    visited[front * 2] = True
            elif i == 3:
                if 1 <= front - 10 <= 1000000 and visited[front-10] == False:
                    Q.append((front-10, check+1))
                    visited[front - 10] = True


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    visited = [False] * 1000001 #방문확인
    Q = deque()
    Q.append((N,0))
    BFS()

    print("#{} {}".format(tc,result))