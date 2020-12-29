def solution(A):
    # write your code in Python 3.6
    s = set()
    for a in A:
        if a in s:
            s.remove(a)
        else:
            s.add(a)
    return s.pop()
