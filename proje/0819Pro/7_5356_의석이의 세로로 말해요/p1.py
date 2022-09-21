import sys
sys.stdin=open('sample_input.txt')

tc = int(input())

for test in range(tc):
    arr = [list(input()) for _ in range(5)]
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr[i]) != len(arr[i+1]):
                while len(arr[i]) != len(arr[i+1]):
                    if len(arr[i])>len(arr[i+1]):
                        arr[i+1].append('')
                    else:
                        arr[i].append('')
                print(arr[j][i])
    # for i in range(len(arr)-1):
    #     for j in range(len(arr[i])):
    #         if len(arr[i]) != len(arr[i+1]):
    #             while len(arr[i]) != len(arr[i+1]):
    #                 arr[i].append('')
    #         print(arr[j][i],end='')
    # print()
