s = 'This is a book'
s_1 = 'is'
N = len(s)
M = len(s_1)

def Bruteforce(s,s_1):
    i = 0
    j = 0
    while j<M and i<N:
        if s[i] != s_1[j]:
            i = i-j
            j = -1
        i += 1
        j += 1

    if j ==M:
        return i-M
    else:
        return -1
print(Bruteforce(s,s_1))
