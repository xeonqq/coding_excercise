def prefix_sum(S):
    index_map = {"A": 0, "C":1, "G":2, "T":3}

    occurance_prefix_sum = [[0]*4 for _ in range(len(S)+1)]
    for i, s in enumerate(S):
        occurance_prefix_sum[i+1] = occurance_prefix_sum[i].copy()
        occurance_prefix_sum[i+1][index_map[s]] +=1
    return occurance_prefix_sum

def list_sub(l1, l2):
    r = []
    for a, b in zip(l1, l2):
        r.append(a-b)
    return r

def min_geno_factor(occurance):
    geno_map = {0: "A", 1: "C", 2: "G", 3: "T"}
    d = {"A": 1, "C":2, "G":3, "T": 4}

    for i, count in enumerate(occurance):
        if count != 0:
            return d[geno_map[i]]

def solution(S, P, Q):
    # write your code in Python 3.6
    prefix_s = prefix_sum(S)
    result = []
    for p, q in zip(P, Q):
        occurance = list_sub(prefix_s[q+1], prefix_s[p])
        factor = min_geno_factor(occurance)
        result.append(factor)
    return result
