import os
import time

def ler_numeros(caminho):
    """Lê números inteiros de um arquivo e retorna como lista."""
    try:
        return [int(l.strip()) for l in open(caminho)]
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return []

def medir_tempo(arquivos, func_sort, nome_arquivo, repeticoes, pasta_resultados="Trabalho 1/resultados"):

    os.makedirs(pasta_resultados, exist_ok=True)
    resultados = []

    # Cabeçalho da tabela no console
    print("=" * 80)
    print(f"{'Arquivo (' + str(repeticoes) + 'Exe.)':<35} {'Qtd. Números':<15} {'Tempo Médio (s)':<15}")
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
            func_sort(nums, tam)
            fim = time.time()
            tempos.append(fim - inicio)

        tempo_medio = sum(tempos) / repeticoes
        resultados.append((arq, tam, tempo_medio))

        # Exibir no console
        print(f"{arq:<45} {tam:<15} {tempo_medio:<15.6f}")

    print("=" * 80)
    print(f"\nResultados salvos em '{pasta_resultados}/{nome_arquivo}'")

    # Salvar no arquivo de forma formatada
    resultado_arquivo = os.path.join(pasta_resultados, nome_arquivo)
    with open(resultado_arquivo, "w") as f:
        f.write("=" * 80 + "\n")
        f.write(f"{'Arquivo (' + str(repeticoes) + ' Exe.)':<35} {'Qtd. Números':<15} {'Tempo Médio (s)':<15}\n")
        f.write("=" * 80 + "\n")
        for arq, q, t in resultados:
            f.write(f"{arq:<45} {q:<15} {t:<15.6f}\n")
        f.write("=" * 80 + "\n")
