import sys
sys.stdin = open('sample_input.txt')

def enq(n):
    global last         # 마지막 노드번호
    last += 1
    heap[last] = n      # 마지막에 값 저장
    c = last            # 부모, 자식 노드
    p = c//2
    while p and heap[p] > heap[c]:  # 부모가 존재하고 부모가 자식보다 더 크다면
        heap[p],heap[c] = heap[c],heap[p]   # 교환
        c = p
        p = c//2

tc = int(input())
for test in range(tc):
    V = int(input())
    arr = list(map(int,input().split()))
    heap = [0] * (V+1)
    last = 0
    while True:
        enq(arr.pop(0))         # 힙에 arr의 데이터를 하나씩 넣음
        if len(arr) == 0:
            break

    result = 0
    while V!=1:
        if heap[V//2] != 0:     # 부모 노드의 값을 result에 더함
            result += heap[V//2]
            V = V//2

    print(f'#{test+1} {result}')