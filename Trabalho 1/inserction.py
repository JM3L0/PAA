import time, os

def insertion_sort(arr, tam):
    for i in range(1, tam):
        chave, j = arr[i], i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
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
        insertion_sort(nums, tam)
        tempo = time.time() - inicio
        
        resultados.append((arq, tam, tempo))
        print(f"{arq}: {tempo:.6f} s")

    with open(os.path.join(pasta_resultados, "tempos_insertion_sort.txt"), "w") as f:
        f.write("Arquivo\tQuantidade\tTempo(s)\n")
        for arq, q, t in resultados:
            f.write(f"{arq}\t{q}\t{t:.6f}\n")
    print(f"\nResultados salvos em '{pasta_resultados}/tempos_insertion_sort.txt'")

arquivos = [f"Trabalho 1/entradas/{tipo}_{n}.txt" 
            for tipo in ["crescente", "decrescente", "aleatorio"] 
            for n in [1,2,4]]

medir_tempo(arquivos)
