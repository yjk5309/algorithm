def solution(strings, n):

    string_sorted = sorted(strings, key = lambda x : (x[n], x))
    
    return string_sorted
