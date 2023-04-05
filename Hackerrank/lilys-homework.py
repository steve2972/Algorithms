def lilysHomework(arr):
    sarr = sorted(arr[:])
    sarr_desc = sorted(arr[:], reverse=True)
    idxs = {v: i for i, v in enumerate(arr)}
    idxs_desc = {v: i for i, v in enumerate(arr)}

    arr1 = arr[:]
    arr2 = arr[:]
    swaps1 = 0
    swaps2 = 0

    for i in range(len(arr)):
        if sarr[i] != arr1[i]:
            j = idxs[sarr[i]]
            arr1[i], arr1[j] = arr1[j], arr1[i]
            idxs[arr1[j]] = j
            idxs[arr1[i]] = i
            swaps1 += 1

        if sarr_desc[i] != arr2[i]:
            j = idxs_desc[sarr_desc[i]]
            arr2[i], arr2[j] = arr2[j], arr2[i]
            idxs_desc[arr2[j]] = j
            idxs_desc[arr2[i]] = i
            swaps2 += 1

    return min(swaps1, swaps2)


print(lilysHomework([7, 15, 12, 3]))