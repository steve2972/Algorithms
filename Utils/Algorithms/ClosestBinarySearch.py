def binary_search_closest(arr, l, r, target):
    # Note, change arr[mid] to > target if descending order
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_closest(arr, l, mid - 1, target)
        else:
            return binary_search_closest(arr, mid + 1, r, target)
    else:
        return l