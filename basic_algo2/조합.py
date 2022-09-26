
def comb(i,k,r):
    if i==r:
        print(p)
    else:
        for j in range(k):
            if used[j] ==0:
                used[j] = 1
                p[i] = arr[j]
                comb(i+1,k,r)
                used[j] = 0

arr = [1,2,3,4,5,6,7]
r = 3
p = [0] * r
used = [0] * len(arr)


comb(0,7,3)