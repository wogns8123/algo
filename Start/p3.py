import sys
sys.stdin=open('input.txt')

tc = int(input())
for test in range(tc):
    s = list(input())

    hex = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A':10,
        'B':11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    dic = {
        '001101': 0,
        '010011': 1,
        '111011': 2,
        '110001': 3,
        '100011': 4,
        '110111': 5,
        '001011': 6,
        '111101': 7,
        '011001': 8,
        '101111': 9,
    }
    # 16진법 -> 10진법
    result = []
    for i in range(len(s)):
        result.append(hex[s[i]])
    # 10진법 -> 2진법
    bin_result = []
    for i in range(len(result)):
        a = bin(result[i])
        b = a[2:]
        while len(b) < 4:
            b = '0' + b
        bin_result.append(b)

    cutting_text = ''.join(bin_result)
    print(cutting_text)

    # 뒤에서부터 보면서 1찾으면 그 뒤를 자름

    for i in range(len(cutting_text)-1, 0, -1):
        if cutting_text[i] == '1':
            cutting_text = cutting_text[:i+1]
            break
    print(cutting_text)
    cutting_list = list(cutting_text)
    cutting_list = cutting_list[::-1]

    cutting_text = ''.join(cutting_list)
    print(cutting_text)

    answer =[]
    for i in range(0,len(cutting_text),6):
        a = cutting_text[i:i+6]
        if len(a)<6:
            continue
        else:
            answer.append(dic[a[::-1]])
    answer = answer[::-1]
    print(*answer)