import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    arr = [list(map(int,input().split())) for _ in range(9)]
    arr2 = list(zip(*arr))
    result = 1
    right = [1,2,3,4,5,6,7,8,9]
    # 가로 세로
    for i in range(9):
        x_arr = [0]*10
        y_arr = [0] * 10
        for j in range(9):
            x_arr[arr[i][j]] += 1
            y_arr[arr[j][i]] += 1


        for k in range(1,10):
            if x_arr[k] != 1:
                result = 0
                break
            if y_arr[k] != 1:
                result = 0
                break

    # window만들기
    for i in range(3):
        for j in range(3):
            arr_window = [0]*10
            for k in range(3):
                for l in range(3):
                    arr_window[arr[3*i+k][3*j+l]] += 1

            for k in range(1,10):
                if arr_window[k] != 1:
                    result =0
                    break
    print(f'#{test+1} {result}')