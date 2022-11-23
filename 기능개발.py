from collections import deque
import math

def solution(progresses, speeds):
    q = deque()
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        q.append(math.ceil((100 - progress) / speed))
        
    d = q[0]
    q.popleft()
    count = 1

    while q:
        if q[0] <= d:
            count += 1
            q.popleft()
        else:
            answer.append(count)
            count = 0
            d = q[0]

    answer.append(count)

    return answer