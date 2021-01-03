def solution(H):
    # write your code in Python 3.6
    stack = []
    stone = 0
    for h in H:

        while len(stack) != 0:
            prev_h = stack[-1]
            if prev_h > h:
                stack.pop(-1)
            else:
                break
        if len(stack) == 0:
            stone +=1 
            stack.append(h)
            continue     
        prev_h = stack[-1] 
  
        if prev_h < h:
            stone+=1
            stack.append(h)

        if prev_h == h:
            continue
    return stone
