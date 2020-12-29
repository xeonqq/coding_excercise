def prepare_factorization(x):
    table = [0] * (x+1)
    for i in range(2, len(table)):
        if table[i]==0:
            multiply=2
            while(i*multiply<=x):
                table[i*multiply] = i
                multiply +=1
    return table

def factorize(x, table): 
    index = x
    factors = []
    while table[index]!=0:
        factors.append(table[index])
        index = index//table[index]
    factors.append(index)
    return factors

def solution(N, P, Q):
    # write your code in Python 3.6
    if not P:
        return []
    factorized_nums = []
    table = prepare_factorization(N)
    #result = [0]*len(P)
    for i in range(0, N+1):
        factorized_nums.append(factorize(i, table))
    table_prefix_sum = []
    for factors in factorized_nums:
        if len(factors) == 2:
            table_prefix_sum.append(1)
        else:
            table_prefix_sum.append(0)
    for i in range(1, len(table_prefix_sum)):
        table_prefix_sum[i] = table_prefix_sum[i] + table_prefix_sum[i-1]
    #print(table_prefix_sum)
    result = []
    for b1, b2 in zip(P, Q):
        result.append(table_prefix_sum[b2] - table_prefix_sum[b1-1])
    return result
