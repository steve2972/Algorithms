def partition(arr, low, hi):
    pivot = low
    for i in range(low+1, hi):
        if arr[i] <= arr[low]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[low] = arr[low], arr[pivot]
    return pivot

def quicksort(arr, low, hi):
    if hi <= low: return
    i = partition(arr, low, hi)
    quicksort(arr, low, i)
    quicksort(arr, i+1, hi)

def mergeSort(array):
    if len(array) <= 1: return
    r = len(array)//2
    L = array[:r]
    M = array[r:]
    mergeSort(L)
    mergeSort(M)

    i = j = k = 0

    while i < len(L) and j < len(M):
        if L[i] < M[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = M[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(M):
        array[k] = M[j]
        j += 1
        k += 1