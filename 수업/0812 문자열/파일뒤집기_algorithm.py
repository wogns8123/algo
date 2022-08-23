a = 'algorithm'

# print(a[::-1])

# reverse_s = ''
# for i in range(len(a)-1, -1, -1):
#     reverse_s = reverse_s + a[i]
# print(reverse_s)

list_s = list(a)
for idx in range(len(a) // 2):
    list_s[idx], list_s[-idx-1] = list_s[-idx-1], list_s[idx]
print(list_s)