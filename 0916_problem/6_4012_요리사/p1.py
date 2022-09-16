import sys
sys.stdin=open('input.txt')

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    food_list = list(range(1,N+1))
    result = []
    for i in range(1<<len(food_list)):
        set = []
        for j in range(len(food_list)):
            if i& (1<<j):
                set.append(arr[j])
        if len(set)==N//2-1\
                :

            result.append(set)
    print(result)
    case = int((factorial(N)//(factorial(N-(N//2)) * factorial(N//2)))//2)
    print(case)