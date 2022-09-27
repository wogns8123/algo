import sys
sys.stdin = open('input.txt')


def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1:
        return array
    pivot, tail = array[0], array[1:]
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = quick_sort(arr)
    print(f'#{test+1} {ans[len(ans)//2]}')
