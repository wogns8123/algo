s = input()
n = len(s)

# result = 0
# for i in range(n//2):
#     if s[i] == s[-i-1]:
#         result = True
#     else:
#         result = False
# print(result)

if s == s[::-1]:
    print(True)
else:
    print(False)

