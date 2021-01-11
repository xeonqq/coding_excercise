def solution(A):
    # write your code in Python 3.6
    max_slice = current_accum = A[0]
    
    for a in A[1:]:
        current_accum = max(current_accum+a,a)
        max_slice = max(current_accum, max_slice)
    return max_slice
