import time
import os

def insertion_sort(arr, tam):

    for i in range(1, tam):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

def ler_numeros_arquivo(caminho_arquivo):
    """Lê números de um arquivo e retorna como lista de inteiros"""
    try:
        with open(caminho_arquivo, "r") as f:
            return [int(linha.strip()) for linha in f.readlines()]
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return []

def medir_tempo_insertion_sort(arquivos, pasta_resultados="Trabalho 1/resultados"):
    """Mede o tempo de execução do Insertion Sort para cada arquivo e salva os resultados"""
    resultados = []

    # Garantir que a pasta resultados exista
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)

    for arquivo in arquivos:
        numeros = ler_numeros_arquivo(arquivo)
        if not numeros:
            continue
        
        tam = len(numeros)# Tamanho do array
        
        inicio = time.time()
        insertion_sort(numeros, tam)
        fim = time.time()
        tempo_execucao = fim - inicio

        resultados.append((arquivo, len(numeros), tempo_execucao))
        print(f"{arquivo}: {tempo_execucao:.6f} segundos")

    # Salvar resultados em um arquivo dentro da pasta resultados
    resultado_arquivo = os.path.join(pasta_resultados, "tempos_insertion_sort.txt")
    with open(resultado_arquivo, "w") as f:
        f.write("Arquivo\tQuantidade\tTempo (s)\n")
        for arquivo, quantidade, tempo in resultados:
            f.write(f"{arquivo}\t{quantidade}\t{tempo:.6f}\n")

    print(f"\nResultados salvos em '{resultado_arquivo}'")

# --- EXEMPLO DE USO ---
arquivos = [
    "Trabalho 1/entradas/crescente_1.txt",
    "Trabalho 1/entradas/crescente_2.txt",
    "Trabalho 1/entradas/crescente_4.txt",
    "Trabalho 1/entradas/decrescente_1.txt",
    "Trabalho 1/entradas/decrescente_2.txt",
    "Trabalho 1/entradas/decrescente_4.txt",
    "Trabalho 1/entradas/aleatorio_1.txt",
    "Trabalho 1/entradas/aleatorio_2.txt",
    "Trabalho 1/entradas/aleatorio_4.txt"
]

medir_tempo_insertion_sort(arquivos)
