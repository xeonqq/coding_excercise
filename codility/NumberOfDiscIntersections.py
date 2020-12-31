def solution(A):
    # write your code in Python 3.6
    events = []
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)]

    events.sort(key=lambda x: (x[0], -x[1]))


    pairs,  active = 0,0
    for event in events:

        if event[1] == 1:
            pairs += active
        active+=event[1]

        
    if pairs > 1e7:
        return -1
    return pairs
