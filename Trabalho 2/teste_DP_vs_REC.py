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

RESULT_FILE = os.path.join(os.path.dirname(__file__), "resultados", "tabela_de_resultados_lcs.csv")
MAX_RECURSIVO = 17  # Limite para executar versão recursiva


# ========================
# UTILITÁRIOS GERAIS
# ========================

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


# ========================
# TRACEMALLOC
# ========================

def iniciar_tracemalloc():
    """Garante início limpo da medição de memória."""
    if tracemalloc.is_tracing():
        tracemalloc.stop()
    tracemalloc.start()


def parar_tracemalloc():
    """Para a medição e retorna pico em MB."""
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / (1024 ** 2)


# ========================
# MEDIÇÕES DP
# ========================

def executar_lcs_dp(X, Y):
    """Executa o algoritmo DP e retorna (lcs, tempo)."""
    start = time.perf_counter()
    L = lcs_dp.lcs_dp(X, Y)
    lcs = lcs_dp.lcs_reconstroi_string(X, Y, L)
    tempo = time.perf_counter() - start
    return lcs, tempo


def medir_lcs_dp(X, Y):
    """Mede tempo e memória da abordagem dinâmica."""
    gc.collect()
    iniciar_tracemalloc()
    lcs, tempo = executar_lcs_dp(X, Y)
    memoria = parar_tracemalloc()
    return lcs, tempo, memoria


# ========================
# MEDIÇÕES RECURSIVAS
# ========================

def executar_lcs_rec(X, Y):
    """Executa o algoritmo recursivo e retorna (lcs, tempo)."""
    start = time.perf_counter()
    lcs = lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))
    tempo = time.perf_counter() - start
    return lcs, tempo


def medir_lcs_rec(X, Y):
    """Mede tempo, memória, chamadas e profundidade da abordagem recursiva."""
    lcs_recursive.cont_calls = 0
    lcs_recursive.max_depth = 0
    
    gc.collect()
    iniciar_tracemalloc()
    lcs, tempo = executar_lcs_rec(X, Y)
    heap_mb = parar_tracemalloc()
    
    total_mb = estimar_memoria_total(heap_mb, lcs_recursive.max_depth)
    chamadas = lcs_recursive.cont_calls
    
    return lcs, tempo, total_mb, chamadas


# ========================
# CÁLCULOS DE RAZÕES
# ========================

def calcular_razao(valor_atual, valor_anterior):
    """Calcula a razão entre dois valores."""
    return valor_atual / valor_anterior if valor_anterior > 0 else 0


def criar_metricas_dp(lcs, tempo, memoria, prev_tempo, prev_memoria):
    """Cria dicionário com métricas do DP."""
    return {
        'lcs_len': len(lcs),
        'tempo': tempo,
        'razao_tempo': calcular_razao(tempo, prev_tempo),
        'memoria': memoria,
        'razao_memoria': calcular_razao(memoria, prev_memoria)
    }


def criar_metricas_rec(lcs, tempo, memoria, chamadas, prev_chamadas):
    """Cria dicionário com métricas do recursivo."""
    return {
        'lcs_len': len(lcs),
        'tempo': tempo,
        'memoria': memoria,
        'chamadas': chamadas,
        'razao_chamadas': calcular_razao(chamadas, prev_chamadas)
    }


# ========================
# FORMATAÇÃO DE SAÍDA
# ========================

def imprimir_teste_inicio(tamanho):
    """Imprime início de um teste."""
    print(f"Teste: Tamanho {tamanho}")


def imprimir_resultado_dp(metricas):
    """Imprime resultados do DP."""
    print(f"[DP]  LCS={metricas['lcs_len']} | "
          f"Tempo={metricas['tempo']:.6f}s ({metricas['razao_tempo']:.2f}x) | "
          f"Mem={metricas['memoria']:.6f}MB ({metricas['razao_memoria']:.2f}x)")


def imprimir_resultado_rec(metricas):
    """Imprime resultados do recursivo."""
    print(f"[Rec] LCS={metricas['lcs_len']} | "
          f"Tempo={metricas['tempo']:.6f}s | "
          f"MemTotal={metricas['memoria']:.6f}MB | "
          f"Chamadas={metricas['chamadas']:,} ({metricas['razao_chamadas']:.2f}x)\n")


def imprimir_resultado_rec_pulado():
    """Imprime que recursivo foi pulado."""
    print("[Rec] Pulado (strings muito grandes)\n")


# ========================
# GERAÇÃO DE RESULTADOS
# ========================

def gerar_linha_resultado_com_rec(tamanho, metricas_dp, metricas_rec):
    """Gera linha de resultado com dados recursivos."""
    return [
        f"Tamanho {tamanho}", tamanho, metricas_dp['lcs_len'],
        metricas_dp['tempo'], metricas_dp['razao_tempo'],
        metricas_dp['memoria'], metricas_dp['razao_memoria'],
        metricas_rec['tempo'], metricas_rec['memoria'],
        metricas_rec['chamadas'], metricas_rec['razao_chamadas']
    ]


def gerar_linha_resultado_sem_rec(tamanho, metricas_dp):
    """Gera linha de resultado sem dados recursivos."""
    return [
        f"Tamanho {tamanho}", tamanho, metricas_dp['lcs_len'],
        metricas_dp['tempo'], metricas_dp['razao_tempo'],
        metricas_dp['memoria'], metricas_dp['razao_memoria'],
        "N/A", "N/A", "N/A", "N/A"
    ]


# ========================
# EXECUÇÃO DOS TESTES
# ========================

def executar_testes(max_tamanho=100):
    """Executa os testes de desempenho e salva os resultados."""
    resultados = []
    prev_tempo_dp = prev_memoria_dp = prev_chamadas_rec = 0
    
    random.seed(42)  # Para reprodutibilidade

    for tamanho in range(1, max_tamanho + 1):
        X, Y = gerar_string_aleatoria(tamanho), gerar_string_aleatoria(tamanho)
        
        imprimir_teste_inicio(tamanho)

        # --- MEDIR DP ---
        lcs_dp, tempo_dp, mem_dp = medir_lcs_dp(X, Y)
        metricas_dp = criar_metricas_dp(
            lcs_dp, tempo_dp, mem_dp, prev_tempo_dp, prev_memoria_dp
        )
        prev_tempo_dp, prev_memoria_dp = tempo_dp, mem_dp
        imprimir_resultado_dp(metricas_dp)

        # --- MEDIR RECURSIVO ---
        if tamanho <= MAX_RECURSIVO:
            lcs_rec, tempo_rec, mem_rec, calls = medir_lcs_rec(X, Y)
            metricas_rec = criar_metricas_rec(
                lcs_rec, tempo_rec, mem_rec, calls, prev_chamadas_rec
            )
            prev_chamadas_rec = calls
            imprimir_resultado_rec(metricas_rec)
            
            linha = gerar_linha_resultado_com_rec(tamanho, metricas_dp, metricas_rec)
            resultados.append(linha)
        else:
            imprimir_resultado_rec_pulado()
            linha = gerar_linha_resultado_sem_rec(tamanho, metricas_dp)
            resultados.append(linha)

    salvar_resultados_csv(resultados)
    print(f"Resultados salvos em '{RESULT_FILE}'")


# ========================
# SALVAMENTO EM CSV
# ========================

def obter_cabecalho_csv():
    """Retorna o cabeçalho do CSV."""
    return [
        "Descricao", "Tamanho", "Comprimento LCS",
        "Tempo DP (s)", "Razao Tempo DP",
        "Mem DP (MB)", "Razao Mem DP",
        "Tempo Rec (s)", "Mem Rec Estimada (MB)",
        "Chamadas Rec", "Razao Crescimento Rec"
    ]


def salvar_resultados_csv(resultados):
    """Salva resultados em arquivo CSV."""
    cabecalho = obter_cabecalho_csv()
    with open(RESULT_FILE, "w", newline="") as f:
        csv.writer(f).writerows([cabecalho] + resultados)


# ========================
# EXECUÇÃO PRINCIPAL
# ========================

if __name__ == "__main__":
    executar_testes()