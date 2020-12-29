def inverse(A):
    r = []
    for a in A:
        if a==0:
            r.append(1)
        else:
            r.append(0)
    return r

def solution(A):
    # write your code in Python 3.6
    

    prefix_sum = inverse(A) 
    
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
    s = 0
    for i, a in enumerate(A):
        if a==1:
            s += prefix_sum[i]
    if s>1e9:
        return -1
    return s
