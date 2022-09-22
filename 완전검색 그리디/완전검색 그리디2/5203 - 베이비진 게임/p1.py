import sys
sys.stdin = open('sample_input.txt')

def f(i, k,arr):
    global ans
    if i ==k:
        run1 = 0
        tri = 0
        if arr[0] == arr[1] and arr[1] == arr[2]:
            tri +=1
        if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
            run1+=1
        if tri + run1 >= 1:
            ans = 1

    else:
        for j in range(k):
            arr[i],arr[j] =arr[j],arr[i]
            f(i+1,k,arr)
            arr[i], arr[j] = arr[j], arr[i]


tc = int(input())
for test in range(tc):
    arr = list(map(int,input().split()))

    first_player = [arr[0],arr[2],arr[4]]
    second_player = [arr[1],arr[3],arr[5]]
    ans = 0
    for i in range(6,12):
        if i%2 ==0 :
            first_player.append(arr[i])
            f(0,len(first_player),first_player)
            if ans:
                ans = 1
                break
        else:
            second_player.append(arr[i])
            f(0, len(second_player),second_player)
            if ans:
                ans = 2
                break
    print(f'#{test+1} {ans}')
