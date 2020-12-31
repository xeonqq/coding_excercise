class Fish(object):
    def __init__(self, size, direction):
        self.size = size
        self.direction = direction

def process(stack):
    if len(stack) == 1:
        return stack
    else:
        while len(stack)>1:
            curr_fish = stack[-1]
            prev_fish = stack[-2]
            if prev_fish.direction == 1 and curr_fish.direction == 0:
                if prev_fish.size > curr_fish.size:
                    stack.pop(-1)
                    break
                else:
                    stack.pop(-2)
            else:
                break;
    return stack


def solution(A, B):
    # write your code in Python 3.6
    stack = []
    for a, b in zip(A,B):
        stack.append(Fish(a,b))
        stack= process(stack)
                    
            
    return len(stack)
