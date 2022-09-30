import sys
sys.stdin=open('sample_input.txt')

di = [-1,1,0,0]
dj = [0,0,-1,1]

tc = int(input())
for test in range(tc):
    N = int(input())
    x_list = []
    y_list = []
    info = []
    for _ in range(N):
        info_1 = list(map(int,input().split()))
        x_list.append(info_1[0])
        y_list.append(info_1[1])
        info.append((info_1[2],info_1[3]))
    min_x = min(x_list)
    min_y = min(y_list)
    for i in range(N):
        x_list[i] -= min_x
        y_list[i] -= min_y


    arr = [[0] * (max(x_list)+1) for _ in range(max(y_list)+1)]
    for i in range(N):
        arr[y_list[i]][x_list[i]]=info[i]

    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]:
                ri, rj = i+di[arr[i][j][0]], j+dj[arr[i][j][0]]
                if ri<0 or N<=ri or rj<0 or N<=rj:
                    continue



    for i in arr:
        print(i)
