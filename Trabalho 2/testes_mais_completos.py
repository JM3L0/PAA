# filepath: c:\Users\jsous\OneDrive\Área de Trabalho\5 Periodo\PAA\Trabalho 2\teste.py
# Arquivo: test_manager.py
"""
Gerenciador de Testes para o Problema da Subsequência Comum Mais Longa (LCS)

- Executa ambos algoritmos (recursivo e DP)
- Mede tempo e memória
- Exporta resultados para arquivo CSV
- Protege contra strings grandes na recursiva
"""
import time
import tracemalloc
import lcs_dp
import lcs_recursive
import csv
import random
import string

RESULT_FILE = "resultados_lcs.csv"


def gerar_string_aleatoria(tamanho):
    """Gera uma string aleatória com caracteres A-Z"""
    return ''.join(random.choices(string.ascii_uppercase, k=tamanho))


def medir_lcs_dp(X, Y):
    tracemalloc.start()
    start = time.perf_counter()
    L = lcs_dp.lcs_dp(X, Y)
    lcs_string = lcs_dp.lcs_reconstroi_string(X, Y, L)
    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return lcs_string, end - start, peak / (1024 ** 2), L


def medir_lcs_rec(X, Y):
    lcs_recursive.cont_calls = 0
    tracemalloc.start()
    start = time.perf_counter()
    lcs_str = lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))
    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return lcs_str, end - start, peak / (1024 ** 2), lcs_recursive.cont_calls


def executar_testes():
    resultados = []
    
    # Gerar testes de tamanho 1 até 100
    for tamanho in range(1, 101): 
        X = gerar_string_aleatoria(tamanho)
        Y = gerar_string_aleatoria(tamanho)
        desc = f"Tamanho {tamanho}"
        
        print(f"Teste: {desc}")
        
        # Teste DP
        lcs_str_dp, tempo_dp, mem_dp, tabela = medir_lcs_dp(X, Y)
        print(f"[DP] Comprimento LCS: {len(lcs_str_dp)} | Tempo: {tempo_dp:.6f}s | Memória: {mem_dp:.6f}MB")
        
        # Teste Recursivo (apenas para <=15)
        if tamanho <= 16:
            lcs_str_rec, tempo_rec, mem_rec, num_calls = medir_lcs_rec(X, Y)
            print(f"[Rec] Comprimento LCS: {len(lcs_str_rec)} | Tempo: {tempo_rec:.6f}s | Memória: {mem_rec:.6f}MB | Recursões: {num_calls}")
            resultados.append([desc, tamanho, lcs_str_dp, tempo_dp, mem_dp, tempo_rec, mem_rec, num_calls])
        else:
            print(f"[Rec] Pulado (strings muito grandes)")
            resultados.append([desc, tamanho, lcs_str_dp, tempo_dp, mem_dp, "N/A", "N/A", "N/A"])
        print()
    
    # Salvar em CSV
    with open(RESULT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Descricao", "Tamanho", "LCS", "Tempo DP (s)", "Mem DP (MB)", "Tempo Rec (s)", "Mem Rec (MB)", "Chamadas Rec"])
        writer.writerows(resultados)
    print(f"Resultados salvos em {RESULT_FILE}")


if __name__ == "__main__":
    executar_testes()