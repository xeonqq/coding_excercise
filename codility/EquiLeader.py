def leader(A):
    stack = []
    

    for a in A:
        if not stack:
            stack.append(a)    
            continue

        if stack[-1] != a:
            stack.pop(-1)
        else:
            stack.append(a)
    if len(stack) > 0:
        return stack[0]
    return None
        
        
def solution(A):
    # write your code in Python 3.6
    l = leader(A)
    if l is None:
        return 0
    prefix_sum = [0] * (len(A)+1)
    for i, a in enumerate(A):
        prefix_sum[i+1] = (a==l)*1 + prefix_sum[i]

    count = 0
    for i in range(len(A)):
        nums_first = i+1
        num_leaders_first = prefix_sum[i+1]-prefix_sum[0]

        nums_second = len(A) - nums_first
        num_leaders_second = prefix_sum[-1]-prefix_sum[i+1]
        if (num_leaders_first > nums_first/2) and (num_leaders_second > nums_second/2):
                count+=1
    return count
