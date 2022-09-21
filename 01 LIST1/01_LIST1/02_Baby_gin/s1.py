tc = int(input())

for test in range(tc):
    s = input()
    arr = [0]*10 # 카운팅

    for i in s:
        arr[int(i)] += 1

    j = 0
    triplet = run = 0
    while j < 10:
        if arr[j]>=3:
            triplet +=1
            arr[j] -= 3
            continue
        j+=1
    j = 0
    while j<=7:
        if arr[j] != 0 and arr[j]==arr[j+1]==arr[j+2]:
            run +=1
            arr[j + 2] -= 1
            arr[j + 1] -= 1
            arr[j] -= 1
            continue
        j += 1
    if triplet + run == 2:
        print(1)
    else:
        print(0)


