def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    d = 0
    if a>b:
        d = gcd(a,b)
    else:
        d = gcd(b,a)
    return a*b/d

def solution(N, M):
    # write your code in Python 3.6
    return int(lcm(N,M)//M)
