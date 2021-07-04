def solution(lottos, win_nums):
    answer = []
    n = 0
    x = [i for i in lottos if i != 0]
    for i in win_nums:
        if i in x:
            n += 1
    d = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    if len(x) == 0:
        answer = [1, 6]
    elif n == 6:
        answer = [1, 1]
    elif n == 0 and len(x) == 6:
        answer = [6, 6]
    else:
        for key, value in d.items():
            if value == n:
                a = n + 6 - len(x)
                answer = [d[a], key]
    return answer
