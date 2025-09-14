def insertion_sort(arr, tam):
    for i in range(1, tam):
        chave, j = arr[i], i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
        print(f"Passo {i}: {arr}")  # Exibe o estado do array após cada inserção
    return arr

def main():
    arr = [5, 3, 2, 4, 1]
    print("Array original:", arr)
    arr = insertion_sort(arr, len(arr))
    print("Array ordenado:", arr)

if __name__ == "__main__":
    main()