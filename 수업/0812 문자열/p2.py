def itoa(number):
    arr = ''
    minus = False
    if number < 0:
        minus = True
        number = number * (-1)
    while number>0:
        arr = chr((number%10) + 48)+arr
        number = number//10

    if minus:
        arr = '-' + arr
    return arr

n = int(input())
for test in range(n):
    s = int(input())
    print(f'#{test+1} {itoa(s)} {type(itoa(s))}')