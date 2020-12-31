def solution(N, A):
    # write your code in Python 3.6
    max_v = 0
    result = [0] * (N+1)
    last_max = 0
    for a in A:
        if a <= N:
            result[a] = max(result[a], last_max)
            result[a] +=1
            if result[a] > max_v:
                max_v = result[a]
        else:
            last_max = max_v
    for i in range(len(result)-1):
        result[i+1] = max(last_max, result[i+1])
    return result[1:]
