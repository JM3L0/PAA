import matplotlib.pyplot as plt
import pandas as pd
import os

RESULT_FILE = os.path.join(os.path.dirname(__file__), "..", "resultados", "tabela_resultados_n_rainhas.csv")
GRAFICOS_DIR = os.path.join(os.path.dirname(__file__), "graficos")

def criar_diretorio():
    if not os.path.exists(GRAFICOS_DIR):
        os.makedirs(GRAFICOS_DIR)

def carregar_dados():
    return pd.read_csv(RESULT_FILE)

def plotar_tempo(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['N'], df['Tempo BT (s)'], marker='o', linewidth=2, label='Backtracking')
    plt.plot(df['N'], df['Tempo Guloso (s)'], marker='s', linewidth=2, label='Guloso')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Tempo (s)', fontsize=12)
    plt.title('Comparacao de Tempo', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "01_tempo.png"), dpi=300)
    print("Grafico '01_tempo.png' salvo")
    plt.close()

def plotar_memoria(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['N'], df['Mem BT (MB)'], marker='o', linewidth=2, label='Backtracking')
    plt.plot(df['N'], df['Mem Guloso (MB)'], marker='s', linewidth=2, label='Guloso')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Memoria (MB)', fontsize=12)
    plt.title('Comparacao de Memoria', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "02_memoria.png"), dpi=300)
    print("Grafico '02_memoria.png' salvo")
    plt.close()

def plotar_solucoes(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['N'], df['Num Solucoes BT'], marker='o', linewidth=2, color='green')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Numero de Solucoes', fontsize=12)
    plt.title('Solucoes Encontradas (Backtracking)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "03_solucoes.png"), dpi=300)
    print("Grafico '03_solucoes.png' salvo")
    plt.close()

def plotar_tempo_log(df):
    plt.figure(figsize=(10, 6))
    plt.semilogy(df['N'], df['Tempo BT (s)'], marker='o', linewidth=2, label='Backtracking')
    plt.semilogy(df['N'], df['Tempo Guloso (s)'], marker='s', linewidth=2, label='Guloso')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Tempo (s) - Log', fontsize=12)
    plt.title('Tempo (Escala Logaritmica)', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "04_tempo_log.png"), dpi=300)
    print("Grafico '04_tempo_log.png' salvo")
    plt.close()

def plotar_sucesso_guloso(df):
    # Verifica qual coluna existe no CSV
    col_valido = None
    for col in df.columns:
        if 'Valido' in col or 'valido' in col.lower():
            col_valido = col
            break
    
    if col_valido:
        df['Sucesso'] = df[col_valido].apply(lambda x: 100 if str(x).lower() == 'sim' else 0)
    else:
        # Se não encontrar, assume todos válidos
        df['Sucesso'] = 100
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['N'], df['Sucesso'], color='orange', alpha=0.7, edgecolor='black')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Taxa de Sucesso (%)', fontsize=12)
    plt.title('Taxa de Sucesso do Algoritmo Guloso', fontsize=14, fontweight='bold')
    plt.ylim(0, 110)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "05_sucesso_guloso.png"), dpi=300)
    print("Grafico '05_sucesso_guloso.png' salvo")
    plt.close()

def main():
    print("=== Gerando Graficos ===\n")
    criar_diretorio()
    df = carregar_dados()
    
    plotar_tempo(df)
    plotar_memoria(df)
    plotar_solucoes(df)
    plotar_tempo_log(df)
    plotar_sucesso_guloso(df)
    
    print("\n=== Graficos gerados ===")

if __name__ == "__main__":
    main()