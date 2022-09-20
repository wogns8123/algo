import sys
sys.stdin = open('sample_input.txt')


def hextobin(n):
    n = int(n, 16)
    n = bin(n)
    n = n[2:]
    while len(n) < 4:
        n = '0' + n
    return n

dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

tc = int(input())
for test in range(tc):
    n, m = map(int, input().split())
    arr = set([input() for _ in range(n)])
    start = 0
    arr = list(arr)
    secret_list = []
    print(arr)

    while True:
        # 암호코드 열 찾기
        for i in range(len(arr)):
            if arr[i] != arr[i + 1]:
                start = i + 1
                break
        # 암호코드 뽑아내기
        start_x = 0
        for i in range(m - 1, 0, -1):
            if arr[[i] != '0':
                start_x = i
                break
        last_x = 0
        for i in range(0, m):
            if arr[start][i] != '0':
                last_x = i
                break
        # 암호 코드

        secret = arr[start][last_x:start_x + 1]
        secret_list.append(secret)

        for i in range(n):
            if secret in arr[i]:
                arr[i] = arr[i].replace(secret,'0'*len(secret))

        if arr == [[0]*m for _ in range(n)]:
            break
    # arr 암호코드 0으로 변환하고 추가 코드 있는 지 확인해야함

    print(secret_list)

    #
    # 암호코드 2진수로 변환
    # secret_result = []
    # for i in range(len(secret)):
    #     secret_result.append(hextobin(secret[i]))
    # secret_result = ''.join(secret_result)
    #
    # while True:
    #     if secret_result[-1] == '0':
    #         secret_result = secret_result[:-1]
    #         secret_result = '0' + secret_result
    #     else:
    #         break
    # while True:
    #     if len(secret_result) % 56 != 0:
    #         if len(secret_result) % 56 < 28:
    #             secret_result = secret_result[1:]
    #         elif len(secret_result) % 56 > 28:  # 56의 배수보다 작은 경우
    #             secret_result = '0' + secret_result
    #     else:
    #         break
    #
    # # 배수 찾기
    # count = 0
    # while True:
    #     count += 1
    #     if 56 * count == len(secret_result):
    #         break
    # secret_result2 = []
    # for i in range(0,len(secret_result),count):
    #     secret_result2.append(secret_result[i])
    # secret_result2 = ''.join(secret_result2)
    #
    #
    # ans_list = []
    # for i in range(0,len(secret_result2),7):
    #      ans_list.append(dic[secret_result2[i:i+7]])
    #
    # odd = 0
    # even = 0
    # for i in range(0,len(ans_list),2):
    #     odd += ans_list[i]
    #     even += ans_list[i+1]
    # result = odd*3 + even
    # if result%10 == 0:
    #     print(f'#{test+1} {sum(ans_list)}')
    # else:
    #     print(f'#{test+1} 0')