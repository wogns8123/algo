arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(4):
            ci = i + di[k]
            cj = j + dj[k]
            if 0<=ci<len(arr) and 0<=cj<len(arr):
                print(print(arr[ci][cj]))
