def solution(arr):
    if 2 < len(arr):
        arr.remove(min(arr))
    else:
        arr = [-1]
        
    return arr