
numbers=[7,4,2,1,3,6,4,7,8]


# for i in range(len(numbers)-1,0,-1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j],numbers[j+1] = numbers[j+1], numbers[j]

# for i in range(len(numbers)):
#     min_idx = i
#     for j in range(i+1,len(numbers)):
#         if numbers[min_idx] > numbers[j]:
#             min_idx = j
#     numbers[i], numbers[min_idx]= numbers[min_idx], numbers[i]
dic = {}
for i in numbers:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
result = []
# for i in range(max(numbers)+1):
#     while i in dic and dic[i] != 0:
#         result.append(i)
#         dic[i] -= 1
# print(result)

for i in range(max(numbers)+1):
    while i in dic and dic[i] != 0:
        result.append(i)
        dic[i] -= 1
print(result)