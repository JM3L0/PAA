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

# Cenários de teste pré-definidos
CENARIOS = [
    ("ABCDGH", "AEDFHR", "Pequeno (6 chars)"),
    ("AGGTAB", "GXTXAYB", "Pequeno (7 chars)"),
    ("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA", "Médio (30 chars)"),
    ("GATTACA" * 5, "TAGACCA" * 5, "Grande (35 chars)"),
]

RESULT_FILE = "resultados_lcs.csv"


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


# ...existing code...
def executar_testes():
    resultados = []
    for X, Y, desc in CENARIOS:
        print(f"Teste: {desc}\nX={X}\nY={Y}")
        # Teste DP
        lcs_str_dp, tempo_dp, mem_dp, tabela = medir_lcs_dp(X, Y)
        print(f"[DP] LCS: {lcs_str_dp} | Tempo: {tempo_dp:.6f}s | Memória: {mem_dp:.6f}MB")
        # Teste Recursivo (apenas para <=15)
        if len(X) <= 15 and len(Y) <= 15:
            lcs_str_rec, tempo_rec, mem_rec, num_calls = medir_lcs_rec(X, Y)
            print(f"[Rec] LCS: {lcs_str_rec} | Tempo: {tempo_rec:.6f}s | Memória: {mem_rec:.6f}MB | Recursões: {num_calls}")
            resultados.append([desc, len(X), len(Y), lcs_str_dp, tempo_dp, mem_dp, tempo_rec, mem_rec, num_calls])
        else:
            print(f"[Rec] Pulado (strings muito grandes)")
            resultados.append([desc, len(X), len(Y), lcs_str_dp, tempo_dp, mem_dp, "N/A", "N/A", "N/A"])
        print()
    
    # Salvar em CSV
    with open(RESULT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Descrição", "Len X", "Len Y", "LCS", "Tempo DP", "Mem DP", "Tempo Rec", "Mem Rec", "Chamadas Rec"])
        writer.writerows(resultados)
    print(f"Resultados salvos em {RESULT_FILE}")


if __name__ == "__main__":
    executar_testes()