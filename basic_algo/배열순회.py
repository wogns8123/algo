arr = [[1,2,3],[4,5,6],[7,8,9]]
m = len(arr)
n = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        n = len(arr[i])
        if i%2 == 0 :
            print(arr[i][j])
        else:
            print(arr[i][n-j-1])


