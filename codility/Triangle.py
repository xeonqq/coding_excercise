def solution(A):
    # write your code in Python 3.6
    a = sorted(A)
    for i in range(len(A)-2):
        if a[i] + a[i+1] > a[i+2]:
            return 1
    return 0
