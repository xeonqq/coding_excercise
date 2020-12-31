def solution(A):
    # write your code in Python 3.6
    a = sorted(A)
    # 3 positive or 3 neg
    s1 = a[-1] * a[-2] * a[-3]

    # 1 positve, 2 big neg
    s2 = a[-1] * a[0] * a[1] 

    return max(s1,s2)
