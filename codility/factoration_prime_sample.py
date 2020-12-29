def prepare_factorization(x):
    table = [0] * (x+1)
    for i in range(2, len(table)):
        if table[i]==0:
            multiply=2
            while(i*multiply<=x):
                table[i*multiply] = i
                multiply +=1
    return table

def solution(x): 
    table = prepare_factorization(x)
    index = x
    factors = []
    while table[index]!=0:
        factors.append(table[index])
        index = index//table[index]
    factors.append(index)
    return factors
        

print(solution(20))
