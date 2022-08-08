n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
    for number in arr[_]:    # 각 문자열 ''
        # triplet 여부확인 
        if arr[_].count(number)>3:
            continue
        # run 
        elif (number-1,number,number+1):
            continue
            if number==8 or number == 9:
                
        

            


    # arr.append(list(input()))
    # for j in arr:       # j는 리스트 속 리스트 
    #     for number in j:    # j의 각 요소 
    #         count=0
    #         if number in j:
    #             count +=1
    #         if count >3 or [number,int(number)-1,int(number)+1] in j:
    #             print(1)
    #         else:
    #             print(0)   