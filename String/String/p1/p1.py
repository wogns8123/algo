tc =int(input())

for test in range(tc):
    a = input()
    list_s = list(a)
    for idx in range(len(a) // 2):
        list_s[idx], list_s[-idx - 1] = list_s[-idx - 1], list_s[idx]

    list_s = ''.join(list_s)
    print(f'#{test+1} {list_s}')