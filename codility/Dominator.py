def solution(A):
    # write your code in Python 3.6
    if not A:
        return -1
    d = dict()
    dominator = None
    max_count = 0
    for i, a in enumerate(A):
        if a not in d:
            d[a]=[i]
        else:
            d[a].append(i)
        if len(d[a])> max_count:
            max_count = len(d[a])
            dominator=a
    if len(d[dominator]) > len(A)/2:
        return d[dominator][0]
    else:
        return -1
