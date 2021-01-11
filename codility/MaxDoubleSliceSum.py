def solution(A):
    # write your code in Python 3.6
    forward_pass = [0]
    backwad_pass = [0]
    max_accum = 0
    for a in A[1:-1]:
        max_accum = max(max_accum+a, 0)
        forward_pass.append(max_accum)
    max_accum = 0
    A.reverse()

    for a in A[1:-1]:
        max_accum = max(max_accum+a, 0)
        backwad_pass.append(max_accum)
    max_slice = 0

    for i in range(1,len(A)-1):
        max_slice = max(max_slice, forward_pass[i-1]+backwad_pass[-1-i])
    return max_slice
