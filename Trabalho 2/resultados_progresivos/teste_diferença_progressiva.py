import time
import tracemalloc
import csv
import random
import string
import gc
import inspect
import sys
import os

# Adiciona a pasta pai ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import lcs_dp
import lcs_recursive

RESULT_FILE = os.path.join(os.path.dirname(__file__),"tabela_resultados_diferenca_progressiva.csv")

NUM_PARES_TESTE = 5

# ========================
# UTILITÁRIOS GERAIS
# ========================

def gerar_string_base(tamanho):
    """Gera uma string base aleatória."""
    return ''.join(random.choices(string.ascii_uppercase, k=tamanho))


def gerar_strings_com_diferenca(string_base, num_diferencas):
    """
    Gera duas strings onde a segunda tem 'num_diferencas' caracteres diferentes.
    Garante que os novos caracteres NÃO formem uma LCS acidental.
    """
    X = string_base
    Y = list(string_base)
    
    # Seleciona posições aleatórias para modificar
    posicoes = random.sample(range(len(Y)), min(num_diferencas, len(Y)))
    
    for pos in posicoes:
        # Encontra um caractere que:
        # 1. É diferente do caractere atual em Y[pos]
        # 2. Não aparece em X (para evitar criar coincidências acidentais)
        caracteres_disponiveis = set(string.ascii_uppercase) - {Y[pos]}
        
        # Remove caracteres que já aparecem em X para evitar LCS acidental
        caracteres_disponiveis -= set(X)
        
        if caracteres_disponiveis:
            novo_char = random.choice(list(caracteres_disponiveis))
        else:
            # Se não houver caracteres únicos, usa qualquer caractere diferente
            novo_char = random.choice(list(set(string.ascii_uppercase) - {Y[pos]}))
        
        Y[pos] = novo_char
    
    return X, ''.join(Y)


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

def medir_lcs_dp(X, Y):
    """Mede tempo e memória da abordagem dinâmica."""
    gc.collect()
    iniciar_tracemalloc()
    
    start = time.perf_counter()
    L = lcs_dp.lcs_dp(X, Y)
    lcs = lcs_dp.lcs_reconstroi_string(X, Y, L)
    tempo = time.perf_counter() - start
    
    memoria = parar_tracemalloc()
    return lcs, tempo, memoria


# ========================
# MEDIÇÕES RECURSIVAS
# ========================

def medir_lcs_rec(X, Y):
    """Mede tempo, memória, chamadas e profundidade da abordagem recursiva."""
    lcs_recursive.cont_calls = 0
    lcs_recursive.max_depth = 0
    
    gc.collect()
    iniciar_tracemalloc()
    
    start = time.perf_counter()
    lcs = lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))
    tempo = time.perf_counter() - start
    
    heap_mb = parar_tracemalloc()
    
    # Estima memória total (heap + stack)
    frame_size = sys.getsizeof(inspect.currentframe()) / (1024 ** 2)
    total_mb = heap_mb + (lcs_recursive.max_depth * frame_size)
    chamadas = lcs_recursive.cont_calls
    
    return lcs, tempo, total_mb, chamadas


# ========================
# FORMATAÇÃO DE SAÍDA
# ========================

def imprimir_teste_inicio(numero_par, diferenca):
    """Imprime início de um teste."""
    print(f"\nPar {numero_par}: {diferenca} caractere(s) diferente(s)")


def imprimir_resultado_dp(lcs_len, tempo, memoria):
    """Imprime resultados do DP."""
    print(f"  [DP]  LCS={lcs_len} | Tempo={tempo:.8f}s | Mem={memoria:.6f}MB")


def imprimir_resultado_rec(lcs_len, tempo, memoria, chamadas):
    """Imprime resultados do recursivo."""
    print(f"  [Rec] LCS={lcs_len} | Tempo={tempo:.8f}s | MemTotal={memoria:.6f}MB | Chamadas={chamadas:,}")


def imprimir_resultado_rec_pulado():
    """Imprime que recursivo foi pulado."""
    print(f"  [Rec] Pulado (strings muito grandes)")


# ========================
# GERAÇÃO DE RESULTADOS
# ========================

def gerar_linha_resultado(numero_par, diferenca, lcs_dp_len, tempo_dp, mem_dp, 
                          lcs_rec_len=None, tempo_rec=None, mem_rec=None, chamadas_rec=None):
    """Gera linha de resultado."""
    return [
        numero_par,
        diferenca,
        lcs_dp_len,
        tempo_dp,
        mem_dp,
        lcs_rec_len if lcs_rec_len is not None else "N/A",
        tempo_rec if tempo_rec is not None else "N/A",
        mem_rec if mem_rec is not None else "N/A",
        chamadas_rec if chamadas_rec is not None else "N/A"
    ]


# ========================
# EXECUÇÃO DOS TESTES
# ========================

def executar_testes(num_pares=100, tamanho_string=100):
    """Executa os testes com diferença progressiva."""
    resultados = []
    
    random.seed(42)  # Para reprodutibilidade
    string_base = gerar_string_base(tamanho_string)
    
    print(f"Executando {num_pares} testes com strings de {tamanho_string} caracteres")
    print(f"String base: {string_base[:50]}...")

    for numero_par in range(1, num_pares + 1):
        # Número de diferenças vai de 0 a 99
        num_diferencas = numero_par - 1
        
        X, Y = gerar_strings_com_diferenca(string_base, num_diferencas)
        
        imprimir_teste_inicio(numero_par, num_diferencas)

        # --- MEDIR DP ---
        lcs_dp, tempo_dp, mem_dp = medir_lcs_dp(X, Y)
        imprimir_resultado_dp(len(lcs_dp), tempo_dp, mem_dp)

        # --- MEDIR RECURSIVO ---
        
        lcs_rec, tempo_rec, mem_rec, calls = medir_lcs_rec(X, Y)
        imprimir_resultado_rec(len(lcs_rec), tempo_rec, mem_rec, calls)
        
        linha = gerar_linha_resultado(numero_par, num_diferencas, len(lcs_dp), 
                                        tempo_dp, mem_dp, len(lcs_rec), tempo_rec, mem_rec, calls)
        
        resultados.append(linha)

    salvar_resultados_csv(resultados)
    print(f"\n✓ Resultados salvos em '{RESULT_FILE}'")


# ========================
# SALVAMENTO EM CSV
# ========================

def obter_cabecalho_csv():
    """Retorna o cabeçalho do CSV."""
    return [
        "Numero Par",
        "Caracteres Diferentes",
        "LCS DP (len)",
        "Tempo DP (s)",
        "Mem DP (MB)",
        "LCS Rec (len)",
        "Tempo Rec (s)",
        "Mem Rec Estimada (MB)",
        "Chamadas Rec"
    ]


def salvar_resultados_csv(resultados):
    """Salva resultados em arquivo CSV."""
    cabecalho = obter_cabecalho_csv()
    
    # Cria diretório se não existir
    os.makedirs(os.path.dirname(RESULT_FILE), exist_ok=True)
    
    with open(RESULT_FILE, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows([cabecalho] + resultados)


# ========================
# EXECUÇÃO PRINCIPAL
# ========================

if __name__ == "__main__":
    executar_testes(num_pares = NUM_PARES_TESTE, tamanho_string = NUM_PARES_TESTE)