def solution(N, stages):
    answer = []
    l = {}
    n = len(stages)
    for i in range(1,N+1):
        a = 0
        for j in stages:
            if i == j:
                a += 1
        if n != 0:
            l[i] = a / n
            n = n-a
        else:
            l[i] = 0

    for i in sorted(l.items(), reverse=True, key = lambda item: item[1]):
        answer.append(i[0])
    return answer
