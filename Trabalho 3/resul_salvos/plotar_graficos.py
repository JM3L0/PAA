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
    plt.figure(figsize=(12, 6))
    plt.plot(df['N'], df['Tempo BT (s)'], marker='o', linewidth=2, label='Backtracking')
    plt.plot(df['N'], df['Tempo Guloso Simples (s)'], marker='s', linewidth=2, label='Guloso Simples')
    plt.plot(df['N'], df['Tempo Guloso Restart (s)'], marker='^', linewidth=2, label='Guloso Restart')
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
    plt.figure(figsize=(12, 6))
    plt.plot(df['N'], df['Mem BT (MB)'], marker='o', linewidth=2, label='Backtracking')
    plt.plot(df['N'], df['Mem Guloso Simples (MB)'], marker='s', linewidth=2, label='Guloso Simples')
    plt.plot(df['N'], df['Mem Guloso Restart (MB)'], marker='^', linewidth=2, label='Guloso Restart')
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
    plt.figure(figsize=(12, 6))
    plt.semilogy(df['N'], df['Tempo BT (s)'], marker='o', linewidth=2, label='Backtracking')
    plt.semilogy(df['N'], df['Tempo Guloso Simples (s)'], marker='s', linewidth=2, label='Guloso Simples')
    plt.semilogy(df['N'], df['Tempo Guloso Restart (s)'], marker='^', linewidth=2, label='Guloso Restart')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Tempo (s) - Log', fontsize=12)
    plt.title('Tempo (Escala Logaritmica)', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "04_tempo_log.png"), dpi=300)
    print("Grafico '04_tempo_log.png' salvo")
    plt.close()

def plotar_sucesso_gulosos(df):
    # Cria uma cópia para não modificar o DataFrame original
    df_temp = df.copy()
    df_temp['Sucesso Simples'] = df_temp['Guloso Simples Valido'].apply(lambda x: 100 if x else 0)
    df_temp['Sucesso Restart'] = df_temp['Guloso Restart Valido'].apply(lambda x: 100 if x else 0)
    
    x = range(len(df_temp))
    largura = 0.35
    
    plt.figure(figsize=(12, 6))
    plt.bar([i - largura/2 for i in x], df_temp['Sucesso Simples'], largura, 
            label='Guloso Simples', alpha=0.8, color='orange', edgecolor='black')
    plt.bar([i + largura/2 for i in x], df_temp['Sucesso Restart'], largura, 
            label='Guloso Restart', alpha=0.8, color='green', edgecolor='black')
    
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Taxa de Sucesso (%)', fontsize=12)
    plt.title('Taxa de Sucesso dos Algoritmos Gulosos', fontsize=14, fontweight='bold')
    plt.xticks(x, df_temp['N'])
    plt.ylim(0, 110)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "05_sucesso_gulosos.png"), dpi=300)
    print("Grafico '05_sucesso_gulosos.png' salvo")
    plt.close()

def plotar_comparacao_gulosos(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['N'], df['Tempo Guloso Simples (s)'], marker='s', linewidth=2, label='Guloso Simples')
    plt.plot(df['N'], df['Tempo Guloso Restart (s)'], marker='^', linewidth=2, label='Guloso Restart')
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Tempo (s)', fontsize=12)
    plt.title('Comparacao entre Gulosos', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "06_comparacao_gulosos.png"), dpi=300)
    print("Grafico '06_comparacao_gulosos.png' salvo")
    plt.close()

def plotar_tabuleiro(tabuleiro, titulo, nome_arquivo):
    n = len(tabuleiro)
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Cria tabuleiro xadrez
    for i in range(n):
        for j in range(n):
            cor = 'white' if (i + j) % 2 == 0 else 'lightgray'
            ax.add_patch(plt.Rectangle((j, n-1-i), 1, 1, facecolor=cor, edgecolor='black'))
    
    # Coloca rainhas
    for linha, coluna in enumerate(tabuleiro):
        if coluna != -1:
            ax.text(coluna + 0.5, n - linha - 0.5, '♛', 
                   fontsize=60//n*8, ha='center', va='center', color='black', weight='bold')
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title(titulo, fontsize=16, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, nome_arquivo), dpi=300, bbox_inches='tight')
    plt.close()

def plotar_exemplos_tabuleiros():
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import n_rainhas_backtracking
    import n_rainhas_guloso
    
    n = 4
    
    # Backtracking - primeira solução
    solucoes_bt = n_rainhas_backtracking.n_rainhas_backtracking(n)
    if solucoes_bt:
        plotar_tabuleiro(solucoes_bt[0], f'Backtracking - N={n} (1ª Solucao)', f'08_tabuleiro_backtracking.png')
        print(f"Grafico '08_tabuleiro_backtracking.png' salvo")
    
    # Guloso Simples
    tabuleiro_simples = n_rainhas_guloso.n_rainhas_guloso_simples(n)
    valido_s = n_rainhas_guloso.eh_valido(tabuleiro_simples)
    titulo_s = f'Guloso Simples - N={n} ({"Valido" if valido_s else "Invalido"})'
    plotar_tabuleiro(tabuleiro_simples, titulo_s, f'09_tabuleiro_guloso_simples.png')
    print(f"Grafico '09_tabuleiro_guloso_simples.png' salvo")
    
    # Guloso com Restart
    tabuleiro_restart = n_rainhas_guloso.n_rainhas_guloso_com_restart(n)
    valido_r = n_rainhas_guloso.eh_valido(tabuleiro_restart)
    titulo_r = f'Guloso com Restart - N={n} ({"Valido" if valido_r else "Invalido"})'
    plotar_tabuleiro(tabuleiro_restart, titulo_r, f'10_tabuleiro_guloso_restart.png')
    print(f"Grafico '10_tabuleiro_guloso_restart.png' salvo")

def plotar_tabela(df):
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('tight')
    ax.axis('off')
    
    # Seleciona apenas colunas sem sucesso
    df_display = df[['N', 'Num Solucoes BT', 'Tempo BT (s)', 'Mem BT (MB)', 
                     'Tempo Guloso Simples (s)', 'Mem Guloso Simples (MB)',
                     'Tempo Guloso Restart (s)', 'Mem Guloso Restart (MB)']].copy()
    
    # Renomeia colunas
    df_display = df_display.rename(columns={
        'N': 'N',
        'Num Solucoes BT': 'Solucoes',
        'Tempo BT (s)': 'T_BT (s)',
        'Mem BT (MB)': 'M_BT (MB)',
        'Tempo Guloso Simples (s)': 'T_Simples (s)',
        'Mem Guloso Simples (MB)': 'M_Simples (MB)',
        'Tempo Guloso Restart (s)': 'T_Restart (s)',
        'Mem Guloso Restart (MB)': 'M_Restart (MB)'
    })
    
    # Formata os dados
    df_display['T_BT (s)'] = df_display['T_BT (s)'].apply(lambda x: f'{x:.6f}')
    df_display['T_Simples (s)'] = df_display['T_Simples (s)'].apply(lambda x: f'{x:.6f}')
    df_display['T_Restart (s)'] = df_display['T_Restart (s)'].apply(lambda x: f'{x:.6f}')
    df_display['M_BT (MB)'] = df_display['M_BT (MB)'].apply(lambda x: f'{x:.4f}')
    df_display['M_Simples (MB)'] = df_display['M_Simples (MB)'].apply(lambda x: f'{x:.4f}')
    df_display['M_Restart (MB)'] = df_display['M_Restart (MB)'].apply(lambda x: f'{x:.4f}')
    
    table = ax.table(cellText=df_display.values, colLabels=df_display.columns,
                     cellLoc='center', loc='center')
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2.5)
    
    # Estiliza header
    for i in range(len(df_display.columns)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Estiliza linhas alternadas
    for i in range(1, len(df_display) + 1):
        for j in range(len(df_display.columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#f0f0f0')
    
    plt.title('Tabela de Resultados - N Rainhas', fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "07_tabela_resultados.png"), dpi=300, bbox_inches='tight')
    print("Grafico '07_tabela_resultados.png' salvo")
    plt.close()

def main():
    print("=== Gerando Graficos ===\n")
    criar_diretorio()
    df = carregar_dados()
    
    plotar_tempo(df)
    plotar_memoria(df)
    plotar_solucoes(df)
    plotar_tempo_log(df)
    plotar_sucesso_gulosos(df)
    plotar_comparacao_gulosos(df)
    plotar_tabela(df)
    plotar_exemplos_tabuleiros()
    
    print("\n=== Graficos gerados ===")

if __name__ == "__main__":
    main()
