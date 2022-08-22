n = [9,8,7,6,5,4,3,2,1]

# for i in range(len(n)-1,0,-1):
#     for j in range(i):
#         if n[j]>n[j+1]:
#             n[j],n[j+1] = n[j+1],n[j]
for i in range(len(n)):
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1] = n[j+1],n[j]
print(n)

