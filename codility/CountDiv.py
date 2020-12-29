from math import *
def solution(A, B, K):
    # write your code in Python 3.6
    multiple_A = ceil(A / K)
    
    multiple_B = floor(B / K)
    return multiple_B - multiple_A+1
