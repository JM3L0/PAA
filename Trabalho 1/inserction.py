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

def medir_tempo(arquivos, pasta_resultados="Trabalho 1/resultados", repeticoes=30):
    os.makedirs(pasta_resultados, exist_ok=True)
    resultados = []

    # Cabeçalho da tabela no console
    print("=" * 80)
    print(f"{'Arquivo':<45} {'Qtd. Números':<15} {'Tempo Médio (s)':<15}")
    print("=" * 80)

    for arq in arquivos:
        nums_orig = ler_numeros(arq)
        if not nums_orig:
            continue
        tam = len(nums_orig)

        tempos = []
        for _ in range(repeticoes):
            nums = nums_orig.copy()
            inicio = time.time()
            insertion_sort(nums, tam)
            fim = time.time()
            tempos.append(fim - inicio)

        tempo_medio = sum(tempos) / repeticoes
        resultados.append((arq, tam, tempo_medio))

        # Exibir no console
        print(f"{arq:<45} {tam:<15} {tempo_medio:<15.6f}")

    print("=" * 80)
    print(f"\nResultados salvos em '{pasta_resultados}/tempos_insertion_sort.txt'")

    # Salvar no arquivo de forma formatada
    resultado_arquivo = os.path.join(pasta_resultados, "tempos_insertion_sort.txt")
    with open(resultado_arquivo, "w") as f:
        f.write("=" * 80 + "\n")
        f.write(f"{'Arquivo':<45} {'Qtd. Números':<15} {'Tempo Médio (s)':<15}\n")
        f.write("=" * 80 + "\n")
        for arq, q, t in resultados:
            f.write(f"{arq:<45} {q:<15} {t:<15.6f}\n")
        f.write("=" * 80 + "\n")

# Lista automática dos arquivos
arquivos = [f"Trabalho 1/entradas/{tipo}_{n}.txt"
            for tipo in ["crescente", "decrescente", "aleatorio"]
            for n in [1, 2, 4]]

# Executa os testes 30 vezes
medir_tempo(arquivos, repeticoes=30)
