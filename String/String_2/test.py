for _ in range(1, 11):
    tc = int(input())
    n = 100
    words = []
    # 가로를 분석하기 위한 words
    # 세로를 쉽게 분석하기 위한 words_h
    for _ in range(n):
        words.append(input())
    words_h = [''.join(i) for i in zip(*words)]
    print(words)
    print(words_h)