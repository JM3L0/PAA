def insertion_sort(arr, tam):
    for i in range(1, tam):
        chave, j = arr[i], i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr



