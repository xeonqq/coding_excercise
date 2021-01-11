def solution(A):
    # write your code in Python 3.6
    diff = []
    for i in range(len(A)-1):
        diff.append(A[i+1] - A[i])
    max_profix = current_profix = 0

    for d in diff:
        current_profix = max(0, d+current_profix)
        max_profix = max(max_profix, current_profix)
    return max_profix
