def solution(scores):
    answer = ''
    n = 0
    s = list(map(list, zip(*scores)))
    for l in s:
        if (l[n] == max(l) or l[n] == min(l)) and l.count(l[n]) == 1:
            l.remove(l[n])
        n += 1
    for i in s:
        r = sum(i)/len(i)
        if r >= 90:
            answer += 'A'
        elif r < 90 and r >= 80:
            answer += 'B'
        elif r < 80 and r >= 70:
            answer += 'C'
        elif r < 70 and r >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer
