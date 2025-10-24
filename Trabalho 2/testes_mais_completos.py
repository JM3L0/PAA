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
import os

RESULT_FILE = os.path.join(os.path.dirname(__file__), "resultados_lcs.csv")


# ------------------------
# 🔹 Funções utilitárias
# ------------------------

def gerar_string_aleatoria(tamanho):
    """Gera uma string aleatória composta por letras maiúsculas (A-Z)."""
    return ''.join(random.choices(string.ascii_uppercase, k=tamanho))


def medir_memoria_frame_mb():
    """Retorna o tamanho médio de um frame de execução em MB."""
    frame = inspect.currentframe()
    tamanho = sys.getsizeof(frame) / (1024 ** 2)
    del frame
    return tamanho


def estimar_memoria_total(heap_mb, max_depth):
    """Soma o uso da heap (medido) com o da stack (estimado)."""
    return heap_mb + (max_depth * medir_memoria_frame_mb())


def iniciar_tracemalloc():
    """Garante início limpo da medição de memória."""
    if tracemalloc.is_tracing():
        tracemalloc.stop()
    tracemalloc.start()


# ------------------------
# 🔹 Medições de desempenho
# ------------------------

def medir_lcs_dp(X, Y):
    """Mede tempo e memória da abordagem dinâmica."""
    gc.collect()
    iniciar_tracemalloc()

    start = time.perf_counter()
    L = lcs_dp.lcs_dp(X, Y)
    lcs = lcs_dp.lcs_reconstroi_string(X, Y, L)
    tempo = time.perf_counter() - start

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return lcs, tempo, peak / (1024 ** 2)


def medir_lcs_rec(X, Y):
    """Mede tempo, memória, chamadas e profundidade da abordagem recursiva."""
    lcs_recursive.cont_calls = 0
    lcs_recursive.max_depth = 0
    gc.collect()
    iniciar_tracemalloc()

    start = time.perf_counter()
    lcs = lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))
    tempo = time.perf_counter() - start

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    heap_mb = peak / (1024 ** 2)
    total_mb = estimar_memoria_total(heap_mb, lcs_recursive.max_depth)

    return lcs, tempo, total_mb, lcs_recursive.cont_calls


# ------------------------
# 🔹 Execução dos testes
# ------------------------

def executar_testes(max_tamanho=100):
    """Executa os testes de desempenho e salva os resultados."""
    resultados = []
    prev_tempo_dp = prev_mem_dp = prev_calls = 0
    random.seed(42)  # Para reprodutibilidade

    for tamanho in range(1, max_tamanho + 1):
        gc.collect()
        X, Y = gerar_string_aleatoria(tamanho), gerar_string_aleatoria(tamanho)
        desc = f"Tamanho {tamanho}"
        print(f"Teste: {desc}")

        # --- DP ---
        lcs_dp_str, tempo_dp, mem_dp = medir_lcs_dp(X, Y)
        razao_tempo_dp = tempo_dp / prev_tempo_dp if prev_tempo_dp else 0
        razao_mem_dp = mem_dp / prev_mem_dp if prev_mem_dp else 0
        prev_tempo_dp, prev_mem_dp = tempo_dp, mem_dp

        print(f"[DP]  LCS={len(lcs_dp_str)} | Tempo={tempo_dp:.6f}s ({razao_tempo_dp:.2f}x) | "
              f"Mem={mem_dp:.6f}MB ({razao_mem_dp:.2f}x)")

        # --- Recursivo ---
        if tamanho <= 10:
            lcs_rec_str, tempo_rec, mem_rec, calls = medir_lcs_rec(X, Y)
            razao_calls = calls / prev_calls if prev_calls else 0
            prev_calls = calls

            print(f"[Rec] LCS={len(lcs_rec_str)} | Tempo={tempo_rec:.6f}s | "
                  f"MemTotal={mem_rec:.6f}MB | Chamadas={calls:,} ({razao_calls:.2f}x)\n")

            resultados.append([
                desc, tamanho, len(lcs_dp_str),
                tempo_dp, razao_tempo_dp, mem_dp, razao_mem_dp,
                tempo_rec, mem_rec, calls, razao_calls
            ])
        else:
            print("[Rec] Pulado (strings muito grandes)\n")
            resultados.append([
                desc, tamanho, len(lcs_dp_str),
                tempo_dp, razao_tempo_dp, mem_dp, razao_mem_dp,
                "N/A", "N/A", "N/A", "N/A"
            ])

    salvar_resultados_csv(resultados)
    print(f"Resultados salvos em '{RESULT_FILE}'")


# ------------------------
# 🔹 Salvamento
# ------------------------

def salvar_resultados_csv(resultados):
    """Salva resultados em arquivo CSV."""
    colunas = [
        "Descricao", "Tamanho", "Comprimento LCS",
        "Tempo DP (s)", "Razao Tempo DP",
        "Mem DP (MB)", "Razao Mem DP",
        "Tempo Rec (s)", "Mem Rec Estimada (MB)",
        "Chamadas Rec", "Razao Crescimento Rec"
    ]
    with open(RESULT_FILE, "w", newline="") as f:
        csv.writer(f).writerows([colunas] + resultados)


# ------------------------
# 🔹 Execução principal
# ------------------------

if __name__ == "__main__":
    executar_testes()
