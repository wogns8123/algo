def strlen(a):
    count = 0
    while True:
        for i in a:
            if i != '\0':
                count += 1
        else:
            break
    return count
a= ['a','b','c','\0']
print(strlen(a))

def strlen_2(a):
    count = 0
    for i in a:
        if i != '\0':
            count += 1
        elif i == '\0':
            continue
    return count
a = ['a','\0','b','\0','c','d']
print(strlen_2(a))