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
    arr = list(set([input() for _ in range(n)]))
    arr.sort()
    arr = arr[1:]
    print(arr)
    print()
    # 리스트를 문자열로
    arr = ''.join(arr)

    secret_list = []
    # 암호코드 뽑기

    # 1. arr의 좌우 '0'을 제거
    arr = arr.strip('0')

    # 2. 암호코드가 여러개일 경우를 고려
    # 0을 제외한 모든 수를 하기 위해
    # end를 만듬
    while True:
        if '0000' in arr:
            secret_list.append(arr[:arr.find('0000')])
            arr = arr.replace(arr[:arr.find('0000')],'')
            arr = arr.lstrip('0')
        else:
            secret_list.append(arr)
            arr = arr.replace(arr, '')
        if len(arr)==0:
            break
    secret_list = list(set(secret_list))
    all_Result = []

    for secret in secret_list:
        # 암호코드 2진수로 변환
        secret_result = []
        for i in range(len(secret)):
            secret_result.append(hextobin(secret[i]))
        secret_result = ''.join(secret_result)

        # 이진수 모습 맞추기
        # secret_result = 마지막이 1이고 앞자리 정리한 2진수
        while True:
            if secret_result[-1] == '0':
                secret_result = secret_result[:-1]
                secret_result = '0' + secret_result
            else:
                break
        while True:
            if len(secret_result) % 56 != 0:
                if len(secret_result) % 56 < 28:
                    secret_result = secret_result[1:]
                elif len(secret_result) % 56 > 28:  # 56의 배수보다 작은 경우
                    secret_result = '0' + secret_result
            else:
                break

        # 배수 찾기
        count = 0
        while True:
            count += 1
            if 56 * count == len(secret_result):
                break

        # secret_result2 = 56자리의 2진수
        secret_result2 = []
        for i in range(0,len(secret_result),count):
            secret_result2.append(secret_result[i])
        secret_result2 = ''.join(secret_result2)

        # print()
        # # print(f'{test + 1} {secret_result2}')
        # print(secret_result2)
        #
        # ans_list = []
        # for i in range(0,len(secret_result2),7):
        #      ans_list.append(dic[secret_result2[i:i+7]])
        # print(ans_list)
        # print(f'{test+1} {ans_list}')
        # odd = 0
        # even = 0
        # for i in range(0,len(ans_list),2):
        #     odd += ans_list[i]
        #     even += ans_list[i+1]
        # result = odd*3 + even
        # if result%10 == 0:
        #     all_Result.append(sum(ans_list))
    print(f'#{test+1} {sum(all_Result)}')