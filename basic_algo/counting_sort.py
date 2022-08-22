arr = [1,2,3,1,2,3,4,5,6,7]
# list를 이용한 방법
# 1. 개수를 세어준다.
# count = [0] * (max(arr)+1)
# for i in arr:
#     count[i] += 1
#
# # 2. count배열의 원소를 누적합으로 갱신
# for i in range(1,len(count)):
#     count[i] += count[i-1]
# print(count)
#
# # result 배열에 원소를 삽입할 것이다.
# result = [0] * (len(arr))
# for i in arr:
#     idx = count[i]
#     result[idx-1] = i
#     count[i] -= 1
# print(result)

# dic
dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
result = []

for i in range(max(arr)+1):
    while i in dic and dic[i] != 0:
        result.append(i)
        dic[i] -= 1
print(result)

