import sys
sys.stdin = open('input.txt')
def qwer(arr):
    def merge_sort(arr):
        global cnt
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left_arr = []
        right_arr = []
        for i in arr[:mid]:
            left_arr.append(i)
        for j in arr[mid:]:
            right_arr.append(j)
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])

        if left_arr[-1] > right_arr[-1]:
            cnt += 1
        return merge(left_arr,right_arr)

    def merge(left_arr, right_arr):
        global cnt
        result = []
        while len(left_arr)>0 or len(right_arr)>0:
            if len(left_arr)>0 and len(right_arr)>0:
                if left_arr[0]<=right_arr[0]:
                    result.append(left_arr.pop(0))
                else:
                    result.append(right_arr.pop(0))
            elif len(left_arr)>0:
                result.append(left_arr.pop(0))
            elif len(right_arr)>0:
                result.append(right_arr.pop(0))
        return result
    return merge_sort(arr)
tc = int(input())
for test in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    sorted_arr = qwer(arr)
    print(f'#{test+1} {sorted_arr[len(sorted_arr)//2]} {cnt}')

