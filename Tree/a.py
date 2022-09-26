# 완전 이진 트리
# n개의 정점을 가진 완전 이진 트리 t1이 있다.
# n번째 방문 정점 번호중 가장 큰값을 새로운 완전 이진 트리 t2의 n번 정점값으로 저장한다.
T = int(input()) # 테스트의 개수
for t in range(1,T+1): # 테스트의 개수만큼 비교한다.
    n = int(input()) # 정점의 개수를 받는다.
    # n개의 정점 1~20
    # 순회한 결과중 가장 큰값을 넣은 이진트리를 만들어 그 이진트리를 중위순회하시오.

    front = [] # 전위 순회한 결과를 넣는다.
    inner = [] # 중위 순회한 결과를 넣는다.
    post = [] # 후위 순회한 결과를 넣는다.
    def front_order(roop): # 전위 순회를 한다.
        front.append(roop) # step 1. 먼저 roop를 넣는다.
        if roop*2 <= n:
            front_order(roop*2) # step 2. 왼쪽 자식으로 들어간다.
        if (roop*2 +1) <= n:
            front_order((roop*2) +1) # step 3. 오른쪽 자식으로 들어간다.

    def in_order(roop): # 중위 순회를 한다.
        if roop*2 <= n: # step 1. 왼쪽 자식으로 들어간다.
            in_order(roop*2)
        inner.append(roop) # step 2. roop를 빼낸다.
        if (roop*2 +1) <= n: # step 3. 오른쪽 자식으로 들어간다.
            in_order((roop*2)+1)

    def post_order(roop): # 후위 순회를 한다.
        if roop*2 <= n: # step 1. 왼쪽 자식으로 들어간다.
            post_order(roop*2)
        if (roop*2 +1) <= n: # step 2. 오른쪽 자식으로 들어간다.
            post_order((roop*2)+1)
        post.append(roop) # step3. roop를 빼낸다.
    roop = 1 # 기본 roop는 곱하기를 하기위해 0 index를 제외한 것부터 시작한다.
    front_order(roop) # 전위 순회
    in_order(roop) # 중위 순회
    post_order(roop) # 후위 순회
    # 각각 순회한 결과를 비교한다.
    result = [0] + [] # 결과중 가장 큰값으로 만들어진 result 완전 이진 트리를 제작한다.
    for i in range(n):
        result.append(max(front[i],inner[i],post[i])) # 비교하면서 각 인덱스에서 가장 큰값을 result에 넣는다.
    print(result)
    def result_in_order(roop): # result 를 중위 순회한 결과를 도출한다.
        if roop*2 <= n:
            result_in_order(roop*2)
        print(result[roop],end=' ')
        if (roop*2 +1) <= n:
            result_in_order((roop*2)+1)
    print(f'#{t}',end=' ') # 출력 양식에 맞게 한다.
    result_in_order(1) # 중위 순회한 결과를 도출한다.
    print() # 다음 테스트 케이스를 위해 한칸 띄운다.