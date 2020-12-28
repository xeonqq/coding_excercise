def solution(A):
    # write your code in Python 3.6
    # pair (num of occurence, num of non dividables)
    result = []
    for _ in range(len(A)*2+1):
        result.append([0, len(A)])
    for a in A:
        result[a][0] +=1
        result[a][1] -=1
        
    #print(result)
    for num, pair in enumerate(result):
        if (pair[0]==0 or num==0):
            continue
        multiply = 2
        while num*multiply <= 2*len(A):
            result[num*multiply][1] -=1*pair[0]
            multiply+=1
    
    final_result = []
    for a in A:
        final_result.append(result[a][1])
    return final_result
