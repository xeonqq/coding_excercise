def solution(A):
    # write your code in Python 3.6
    max_a = max(A)
    exist = [False]*(max_a+1)
    all_neg = True
    for a in A:
        if a>0:
            exist[a] = True
            all_neg = False
    if all_neg:
        return 1        
    for i, e in enumerate(exist[1:]):
        if e is False:
            return i+1
    return max_a+1
