import time
import tracemalloc
import csv
import gc
import sys
import os

TAMANHOS_TESTE = 14

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import n_rainhas_backtracking
import n_rainhas_guloso

RESULT_FILE = os.path.join(os.path.dirname(__file__), "tabela_resultados_n_rainhas.csv")

def medir_backtracking(n):
    gc.collect()
    tracemalloc.start()
    inicio = time.perf_counter()
    
    solucoes = n_rainhas_backtracking.n_rainhas_backtracking(n)
    
    tempo = time.perf_counter() - inicio
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return len(solucoes), tempo, pico / (1024 ** 2)

def medir_guloso_simples(n):
    gc.collect()
    tracemalloc.start()
    inicio = time.perf_counter()
    
    tabuleiro = n_rainhas_guloso.n_rainhas_guloso_simples(n)
    valido = n_rainhas_guloso.eh_valido(tabuleiro)
    
    tempo = time.perf_counter() - inicio
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return valido, tempo, pico / (1024 ** 2)

def medir_guloso_com_restart(n):
    gc.collect()
    tracemalloc.start()
    inicio = time.perf_counter()
    
    tabuleiro = n_rainhas_guloso.n_rainhas_guloso_com_restart(n)
    valido = n_rainhas_guloso.eh_valido(tabuleiro)
    
    tempo = time.perf_counter() - inicio
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return valido, tempo, pico / (1024 ** 2)

def executar_testes():
    
    tamanhos = list(range(4, TAMANHOS_TESTE + 1))
    resultados = []
    
    print("=== Teste Backtracking vs Guloso Simples vs Guloso com Restart ===\n")
    
    for n in tamanhos:
        print(f"Testando n = {n}...")
        
        num_sol, tempo_bt, mem_bt = medir_backtracking(n)
        valido_s, tempo_gs, mem_gs = medir_guloso_simples(n)
        valido_r, tempo_gr, mem_gr = medir_guloso_com_restart(n)
        
        resultados.append({
            'N': n,
            'Num Solucoes BT': num_sol,
            'Tempo BT (s)': tempo_bt,
            'Mem BT (MB)': mem_bt,
            'Tempo Guloso Simples (s)': tempo_gs,
            'Mem Guloso Simples (MB)': mem_gs,
            'Guloso Simples Valido': valido_s,
            'Tempo Guloso Restart (s)': tempo_gr,
            'Mem Guloso Restart (MB)': mem_gr,
            'Guloso Restart Valido': valido_r
        })
        
        print(f"  BT: {tempo_bt:.6f}s, {num_sol} solucoes")
        print(f"  Guloso Simples: {tempo_gs:.6f}s, valido={valido_s}")
        print(f"  Guloso Restart: {tempo_gr:.6f}s, valido={valido_r}\n")
    
    salvar_resultados(resultados)

def salvar_resultados(resultados):
    with open(RESULT_FILE, 'w', newline='', encoding='utf-8') as f:
        campos = ['N', 'Num Solucoes BT', 'Tempo BT (s)', 'Mem BT (MB)', 
                  'Tempo Guloso Simples (s)', 'Mem Guloso Simples (MB)', 'Guloso Simples Valido',
                  'Tempo Guloso Restart (s)', 'Mem Guloso Restart (MB)', 'Guloso Restart Valido']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
    print(f"Resultados salvos: {RESULT_FILE}")

if __name__ == "__main__":
    executar_testes()
