def solution(left, right):
    answer = 0
    l = []
    measure = []
    while right >= left:
        l.append(left)
        left += 1
    
    count = 0
    for i in l:
        for a in range(1, i+1): 
            if i == a:
                count += 1
            elif i % a == 0: 
                count += 1
        measure.append(count)
        count = 0
    
    for i in range(len(l)):
        if measure[i] % 2 == 0:
            answer += l[i]
        else:
            answer -= l[i]
    return answer
