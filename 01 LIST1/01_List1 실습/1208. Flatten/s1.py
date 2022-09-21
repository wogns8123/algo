import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블정렬
    for i in range(99, 0, -1):  # 구간의 끝 인덱스
        for j in range(i):  # 인접 원소 중 왼쪽 원소 인덱스
            if arr[j] > arr[j+1]:  # 오름차순, 더 큰 수를 오른쪽으로
                arr[j], arr[j+1] = arr[j + 1], arr[j]
    for i in range(N):
        arr[-1] -= 1            # 최대값
        arr[0] += 1             # 최소값
        for j in range(99, 0, -1):  # 한번 시행하면 다시 정렬
            for k in range(j):
                if arr[k] > arr[k + 1]:
                    arr[k], arr[k + 1] = arr[k + 1], arr[k]
    print(f'#{tc+1} {arr[-1] - arr[0]}')