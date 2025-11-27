import time
import tracemalloc
import csv
import gc
import sys
import os

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

def medir_guloso(n):
    gc.collect()
    tracemalloc.start()
    inicio = time.perf_counter()
    
    tabuleiro = n_rainhas_guloso.n_rainhas_guloso(n)
    valido = n_rainhas_guloso.eh_valido(tabuleiro)
    
    tempo = time.perf_counter() - inicio
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return valido, tempo, pico / (1024 ** 2)

def executar_testes():
    tamanhos = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    resultados = []
    
    print("=== Teste Backtracking vs Guloso ===\n")
    
    for n in tamanhos:
        print(f"Testando n = {n}...")
        
        num_sol, tempo_bt, mem_bt = medir_backtracking(n)
        valido, tempo_gl, mem_gl = medir_guloso(n)
        
        razao_tempo = tempo_bt / tempo_gl if tempo_gl > 0 else 0
        
        resultados.append({
            'N': n,
            'Num Solucoes BT': num_sol,
            'Tempo BT (s)': tempo_bt,
            'Mem BT (MB)': mem_bt,
            'Tempo Guloso (s)': tempo_gl,
            'Mem Guloso (MB)': mem_gl,
            'Guloso Valido': valido,
            'Razao Tempo (BT/Guloso)': razao_tempo
        })
        
        print(f"  BT: {tempo_bt:.6f}s, {num_sol} solucoes")
        print(f"  Guloso: {tempo_gl:.6f}s, valido={valido}\n")
    
    salvar_resultados(resultados)

def salvar_resultados(resultados):
    with open(RESULT_FILE, 'w', newline='', encoding='utf-8') as f:
        campos = ['N', 'Num Solucoes BT', 'Tempo BT (s)', 'Mem BT (MB)', 
                  'Tempo Guloso (s)', 'Mem Guloso (MB)', 'Guloso Valido', 'Razao Tempo (BT/Guloso)']
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
    print(f"Resultados salvos: {RESULT_FILE}")

if __name__ == "__main__":
    executar_testes()
