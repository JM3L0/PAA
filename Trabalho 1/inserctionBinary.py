import time, os

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

def ler_numeros(caminho):
    try:
        return [int(l.strip()) for l in open(caminho)]
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return []

def medir_tempo(arquivos, pasta_resultados="Trabalho 1/resultados"):
    os.makedirs(pasta_resultados, exist_ok=True)
    resultados = []

    for arq in arquivos:
        nums = ler_numeros(arq)
        if not nums: continue
        tam = len(nums)
        
        inicio = time.time()
        binary_insertion_sort(nums, tam)
        tempo = time.time() - inicio
        
        resultados.append((arq, tam, tempo))
        print(f"{arq}: {tempo:.6f} s")

    with open(os.path.join(pasta_resultados, "tempos_binary_insertion_sort.txt"), "w") as f:
        f.write("Arquivo\tQuantidade\tTempo(s)\n")
        for arq, q, t in resultados:
            f.write(f"{arq}\t{q}\t{t:.6f}\n")
    print(f"\nResultados salvos em '{pasta_resultados}/tempos_binary_insertion_sort.txt'")

arquivos = [f"Trabalho 1/entradas/{tipo}_{n}.txt" 
            for tipo in ["crescente", "decrescente", "aleatorio"] 
            for n in [1,2,4]]

medir_tempo(arquivos)
