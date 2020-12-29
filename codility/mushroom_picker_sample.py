def prefix_sum(A):
    s = A.copy()
    for i in range(1, len(A)):
        s[i] = s[i] + s[i-1]
    return s
        
def mushrooms(A, k, m):
    s = prefix_sum(A)
    result = 0
    # go left p steps
    pos = -1
    for p in range(min(k, m)):
        left = k - p
        right = min(max(k -p+ m-p,k), len(A)-1)
        count = s[right] - s[left] + A[left]
        if count > result:
            result = count
            pos = left

    # go right
    for p in range(min(len(A)-1-k, m)):
        right = k + p
        left = max(min(k + p-  (m-p), k),0)
        count = s[right] - s[left] + A[left]
        if count > result:
            result = count
            pos = left
    return result, pos

A = [2,3,7,5,1,3,9]
m, pos = mushrooms(A, 4, 6) 
print(m, " expected: 25")
print(pos," expected: 2")
