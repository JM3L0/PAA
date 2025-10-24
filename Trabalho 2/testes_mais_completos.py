import time
import tracemalloc
import lcs_dp
import lcs_recursive
import csv
import random
import string
import gc
import inspect
import sys

RESULT_FILE = "resultados_lcs.csv"


def gerar_string_aleatoria(tamanho):
    """Gera uma string aleatória com caracteres A-Z"""
    return ''.join(random.choices(string.ascii_uppercase, k=tamanho))


def estimar_memoria_real(mem_heap_mb, max_depth):
    """
    Estima o uso real de memória considerando:
      - heap medido pelo tracemalloc (mem_heap_mb)
      - stack (profundidade * tamanho médio de um frame)
    """
    frame = inspect.currentframe()
    tamanho_frame_mb = sys.getsizeof(frame) / (1024 ** 2)
    del frame  # libera referência ao frame atual
    mem_total = mem_heap_mb + (max_depth * tamanho_frame_mb)
    return mem_total


def medir_lcs_dp(X, Y):
    """Mede tempo e memória da abordagem DP"""
    gc.collect()

    if tracemalloc.is_tracing():
        tracemalloc.stop()
    tracemalloc.start()

    start = time.perf_counter()
    L = lcs_dp.lcs_dp(X, Y)
    lcs_string = lcs_dp.lcs_reconstroi_string(X, Y, L)
    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    mem_usada = peak / (1024 ** 2)
    tracemalloc.stop()

    return lcs_string, end - start, mem_usada, L


def medir_lcs_rec(X, Y):
    """Mede tempo, memória, chamadas e profundidade da recursão"""
    lcs_recursive.cont_calls = 0
    lcs_recursive.max_depth = 0
    gc.collect()

    if tracemalloc.is_tracing():
        tracemalloc.stop()
    tracemalloc.start()

    start = time.perf_counter()
    lcs_str = lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))
    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    mem_heap_mb = peak / (1024 ** 2)
    tracemalloc.stop()

    num_calls = lcs_recursive.cont_calls
    max_depth = lcs_recursive.max_depth

    # Estima memória total real (heap + stack)
    mem_usada_total = estimar_memoria_real(mem_heap_mb, max_depth)

    return lcs_str, end - start, mem_usada_total, num_calls


def executar_testes():
    """Executa os testes de desempenho e grava resultados em CSV"""
    resultados = []
    prev_calls = 0
    prev_mem_dp = 0
    prev_tempo_dp = 0

    for tamanho in range(1, 101):
        gc.collect()

        X = gerar_string_aleatoria(tamanho)
        Y = gerar_string_aleatoria(tamanho)
        desc = f"Tamanho {tamanho}"

        print(f"Teste: {desc}")

        # DP
        lcs_str_dp, tempo_dp, mem_dp, tabela = medir_lcs_dp(X, Y)
        razao_mem_dp = mem_dp / prev_mem_dp if prev_mem_dp > 0 else 0
        razao_tempo_dp = tempo_dp / prev_tempo_dp if prev_tempo_dp > 0 else 0
        prev_mem_dp = mem_dp
        prev_tempo_dp = tempo_dp

        print(f"[DP] LCS: {len(lcs_str_dp)} | Tempo: {tempo_dp:.6f}s (Razão: {razao_tempo_dp:.2f}x) | "
              f"Memória: {mem_dp:.6f}MB (Razão: {razao_mem_dp:.2f}x)")

        # Recursiva
        if tamanho <= 14:
            lcs_str_rec, tempo_rec, mem_rec, num_calls = medir_lcs_rec(X, Y)
            razao = num_calls / prev_calls if prev_calls > 0 else 0
            prev_calls = num_calls

            print(f"[Rec] LCS: {len(lcs_str_rec)} | Tempo: {tempo_rec:.6f}s | "
                  f"Memória Estimada Total: {mem_rec:.6f}MB | Chamadas: {num_calls:,} (Razão: {razao:.2f}x)")
            resultados.append([desc, tamanho, len(lcs_str_dp), tempo_dp, razao_tempo_dp, mem_dp,
                               razao_mem_dp, tempo_rec, mem_rec, num_calls, razao])
        else:
            print("[Rec] Pulado (strings muito grandes)")
            resultados.append([desc, tamanho, len(lcs_str_dp), tempo_dp, razao_tempo_dp, mem_dp,
                               razao_mem_dp, "", "", "", ""])
        print()

    # Salvar CSV
    with open(RESULT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Descricao", "Tamanho", "Comprimento LCS", "Tempo DP (s)", "Razao Tempo DP",
            "Mem DP (MB)", "Razao Mem DP", "Tempo Rec (s)", "Mem Rec Estimada (MB)",
            "Chamadas Rec", "Razao Crescimento Rec"
        ])
        writer.writerows(resultados)

    print(f"Resultados salvos em {RESULT_FILE}")


if __name__ == "__main__":
    executar_testes()
