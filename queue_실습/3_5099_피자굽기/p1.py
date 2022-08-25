import sys
sys.stdin = open('sample_input.txt')

tc = int(input())
for test in range(tc):
    fire, piz = map(int,input().split())
    arr = list(map(int,input().split()))
    arr_piz = [0] * (piz)
    for i in range(piz):
        arr_piz[i] = [i+1,arr[i]]   # 피자번호, 치즈

    fire_arr = []       # queue
    while True:
        # 화덕 수 만큼 fire_arr의 요소 넣기
        if len(fire_arr) < fire:                    # 화덕 안의 피자 수가 가용피자수보다 적을 때
            if len(arr_piz) > 0:                    # 남은 피자가 있으면
                fire_arr.append(arr_piz.pop(0))     # 화덕에 추가
            else:
                while True:
                    plus = fire_arr.pop(0)
                    plus[1] = plus[1] // 2
                    #print(plus)
                    if plus[1] != 0:
                        fire_arr.append(plus)
                    if len(fire_arr) == 1:
                        print(f"#{test + 1} {fire_arr[0][0]}")
                        break
                break
        else:                               # 화덕
            for i in range(fire):           #
                plus = fire_arr.pop(0)      # 피자 치즈 확인
                plus[1] = plus[1] // 2      # 치즈 녹임
                #print(plus)
                if plus[1] != 0:            # 0 아니면 다시 화덕으로
                    fire_arr.append(plus)
                else:                       # 0이면 뺌
                    break


