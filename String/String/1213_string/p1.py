import sys
sys.stdin = open('test_input.txt','rt',encoding='UTF8')

for test in range(10):
    number = int(input())
    arr = input()
    arr_2 = input()
    count = 0

    for i in range(len(arr_2)-len(arr)+1):
        if arr == arr_2[i:i+len(arr)]:
            count+=1
    # for i in range(len(arr_2)-len(arr)+1):
    #     for j in range(len(arr)):
    #         if arr_2[i+j] != arr[j]:
    #             break
    #     else:
    #         count+=1
    print(f'#{test+1} {count}')
