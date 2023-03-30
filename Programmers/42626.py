def heapify(arr, i):
    l, r = 2*i+1, 2*i+2
    
    if r < len(arr):
        if arr[i] > arr[l] or arr[i] > arr[r]:
            if arr[l] < arr[r]:
                arr[i], arr[l] = arr[l], arr[i]
                heapify(arr, l)
            else:
                arr[i], arr[r] = arr[r], arr[i]
                heapify(arr, r)
    elif l < len(arr):
        if arr[l] < arr[i]:
            arr[i], arr[l] = arr[l], arr[i]
            heapify(arr, l)


def build(arr):
    for i in range(len(arr)//2, -1, -1): 
        heapify(arr, i)

def pop(arr):
    popped = arr[0]
    arr[0] = arr[-1]
    arr = arr[:-1]
    heapify(arr, 0)
    return popped, arr

def insert(arr, n):
    arr.append(n)
    cur = len(arr) - 1
    while arr[cur] < arr[(cur - 2 + (cur%2))//2]:
        nc = (cur - 2 + (cur%2))//2
        arr[cur], arr[nc] = arr[nc], arr[cur]
        cur = (cur - 2 + (cur%2))//2

import math
from io import StringIO
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return

def solution_old(arr, k):
    if min(arr) >= k: return 0
    build(arr)
    num = 0
    while arr[0] < k:
        a, arr= pop(arr)
        b, arr = pop(arr)
        if a >= k: return num
        new = a + 2*b
        insert(arr, new)
        if len(arr) == 1:
            return -1
        num += 1
    return num

import heapq
def solution(scoville, k):
    scoville.sort()
    heapq.heapify(scoville)
    if scoville[0] >= k: return 0
    answer = 0
    while scoville[0] < k:
        if len(scoville) == 1: return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
    return answer

    
    


import random
max_num = int(20)
scoville = [random.randint(0, max_num) for _ in range(max_num)]
k = random.randint(0, max_num)

print(solution([1, 2, 3, 9, 10, 12], 7))