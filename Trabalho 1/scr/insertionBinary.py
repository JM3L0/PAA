def binary_search(arr, chave, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < chave:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr, tam):
    for i in range(1, tam):
        chave = arr[i]
        pos = binary_search(arr, chave, 0, i)
        for j in range(i, pos, -1):
            arr[j] = arr[j-1]
        arr[pos] = chave
    return arr

