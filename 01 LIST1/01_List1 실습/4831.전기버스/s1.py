tc = int(input())

for i in range(tc):
    # K : 최대 이동 가능 정류장 수
    # N = 종점까지
    # M = 충전기 설치 개수
    K, N, M = list(map(int, input().split()))
    stop_list = list(map(int, input().split()))
    count = 0
    start = 0

    while start + K < N:                    # 현위치 + K가 전체길이보다 작을 때
        for turn in range(K,0,-1):          # turn은 K값에서 역순으로 -1한 값
            if (start + turn) in stop_list: # 현위치 + turn이 stop_list에 있으면 충전가능
                start += turn
                count += 1
                break
        else:
            count = 0
            break
    print(f'#{i + 1} {count}')
