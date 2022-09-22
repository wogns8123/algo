import sys
sys.stdin = open('input.txt')

def change(arr,i,j):
    arr[i], arr[j] = arr[j],arr[i]
    return arr

tc = int(input())
for test in range(tc):
    arr = list(input().split())
    n = list(arr[0])
    change = int(arr[1])
    change_number = 0

    while True:
        for i in range(len(n)-1):
            min_idx = i
            for j in range(i+1,len(n)):
                if n[j] > n[min_idx]:
                    min_idx = j
                    change_number +=1
            n[i], n[min_idx]=n[min_idx],n[i]
            if change<=change_number:
                break
        if change <= change_number:
            break
    print(n)
    # while change>=change_number:
    #     for i in range(len(n)):
    #         if n[i] != max(n):
    #             n[i], n[n.index(max(n))] = n[n.index(max(n))],n[i]
    #         change_number+=1
    # print(n)




