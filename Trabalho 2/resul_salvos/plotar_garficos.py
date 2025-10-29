import matplotlib.pyplot as plt
import pandas as pd
import os

RESULT_FILE = os.path.join(os.path.dirname(__file__), "tabela_de_resultados_lcs.csv")
GRAFICOS_DIR = os.path.join(os.path.dirname(__file__), "graficos")


# ========================
# PREPARAÇÃO
# ========================

def criar_diretorio_graficos():
    """Cria diretório para salvar gráficos se não existir."""
    if not os.path.exists(GRAFICOS_DIR):
        os.makedirs(GRAFICOS_DIR)
    print(f"Gráficos serão salvos em '{GRAFICOS_DIR}'")


def carregar_dados():
    """Carrega dados do arquivo CSV."""
    return pd.read_csv(RESULT_FILE)


# ========================
# GRÁFICOS INDIVIDUAIS POR COLUNA
# ========================

def plotar_tamanho(df):
    """Plota coluna Tamanho."""
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Tamanho'], marker='o', linewidth=2, color='blue')
    plt.xlabel('Iteração', fontsize=12)
    plt.ylabel('Tamanho da String', fontsize=12)
    plt.title('Tamanho da String por Iteração', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "01_tamanho.png"), dpi=300)
    print("✅ Gráfico '01_tamanho.png' salvo")
    plt.close()


def plotar_comprimento_lcs(df):
    """Plota coluna Comprimento LCS."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tamanho'], df['Comprimento LCS'], marker='o', linewidth=2, color='green')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Comprimento do LCS', fontsize=12)
    plt.title('Comprimento do LCS', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "02_comprimento_lcs.png"), dpi=300)
    print("✅ Gráfico '02_comprimento_lcs.png' salvo")
    plt.close()


def plotar_tempo_dp(df):
    """Plota coluna Tempo DP (s)."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tamanho'], df['Tempo DP (s)'], marker='o', linewidth=2, color='blue')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Tempo (segundos)', fontsize=12)
    plt.title('Tempo de Execução - DP', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "03_tempo_dp.png"), dpi=300)
    print("✅ Gráfico '03_tempo_dp.png' salvo")
    plt.close()


def plotar_razao_tempo_dp(df):
    """Plota coluna Razao Tempo DP."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tamanho'], df['Razao Tempo DP'], marker='o', linewidth=2, color='cyan')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Razão de Crescimento', fontsize=12)
    plt.title('Razão de Crescimento de Tempo - DP', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "04_razao_tempo_dp.png"), dpi=300)
    print("✅ Gráfico '04_razao_tempo_dp.png' salvo")
    plt.close()


def plotar_memoria_dp(df):
    """Plota coluna Mem DP (MB)."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tamanho'], df['Mem DP (MB)'], marker='o', linewidth=2, color='green')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Memória (MB)', fontsize=12)
    plt.title('Uso de Memória - DP', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "05_memoria_dp.png"), dpi=300)
    print("✅ Gráfico '05_memoria_dp.png' salvo")
    plt.close()


def plotar_razao_memoria_dp(df):
    """Plota coluna Razao Mem DP."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tamanho'], df['Razao Mem DP'], marker='o', linewidth=2, color='lightgreen')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Razão de Crescimento', fontsize=12)
    plt.title('Razão de Crescimento de Memória - DP', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "06_razao_memoria_dp.png"), dpi=300)
    print("✅ Gráfico '06_razao_memoria_dp.png' salvo")
    plt.close()


def plotar_tempo_rec(df):
    """Plota coluna Tempo Rec (s)."""
    df_com_rec = df[df['Tempo Rec (s)'] != 'N/A']
    if df_com_rec.empty:
        print("⚠️ Sem dados: Tempo Rec (s)")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Tempo Rec (s)'].astype(float), 
             marker='s', linewidth=2, color='red')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Tempo (segundos)', fontsize=12)
    plt.title('Tempo de Execução - Recursivo', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "07_tempo_rec.png"), dpi=300)
    print("✅ Gráfico '07_tempo_rec.png' salvo")
    plt.close()


def plotar_memoria_rec(df):
    """Plota coluna Mem Rec Estimada (MB)."""
    df_com_rec = df[df['Mem Rec Estimada (MB)'] != 'N/A']
    if df_com_rec.empty:
        print("⚠️ Sem dados: Mem Rec Estimada (MB)")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Mem Rec Estimada (MB)'].astype(float),
             marker='s', linewidth=2, color='orange')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Memória (MB)', fontsize=12)
    plt.title('Uso de Memória - Recursivo', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "08_memoria_rec.png"), dpi=300)
    print("✅ Gráfico '08_memoria_rec.png' salvo")
    plt.close()


def plotar_chamadas_rec(df):
    """Plota coluna Chamadas Rec."""
    df_com_rec = df[df['Chamadas Rec'] != 'N/A']
    if df_com_rec.empty:
        print("⚠️ Sem dados: Chamadas Rec")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Chamadas Rec'].astype(float),
             marker='s', linewidth=2, color='purple')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Número de Chamadas', fontsize=12)
    plt.title('Número de Chamadas Recursivas', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "09_chamadas_rec.png"), dpi=300)
    print("✅ Gráfico '09_chamadas_rec.png' salvo")
    plt.close()


def plotar_razao_crescimento_rec(df):
    """Plota coluna Razao Crescimento Rec."""
    df_com_rec = df[df['Razao Crescimento Rec'] != 'N/A']
    if df_com_rec.empty:
        print("⚠️ Sem dados: Razao Crescimento Rec")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Razao Crescimento Rec'].astype(float),
             marker='s', linewidth=2, color='magenta')
    plt.xlabel('Tamanho da String', fontsize=12)
    plt.ylabel('Razão de Crescimento', fontsize=12)
    plt.title('Razão de Crescimento - Chamadas Recursivas', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "10_razao_crescimento_rec.png"), dpi=300)
    print("✅ Gráfico '10_razao_crescimento_rec.png' salvo")
    plt.close()

def plotar_comparacao_tempo_dp_vs_rec(df):
    """Plota comparação unificada de tempo DP vs Recursivo."""
    df_com_rec = df[df['Tempo Rec (s)'] != 'N/A'].copy()
    
    if df_com_rec.empty:
        print("⚠️ Sem dados: Comparação DP vs Rec")
        return
    
    df_com_rec['Tempo Rec (s)'] = df_com_rec['Tempo Rec (s)'].astype(float)
    df_com_rec['Tempo DP (s)'] = df_com_rec['Tempo DP (s)'].astype(float)
    
    plt.figure(figsize=(12, 7))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Tempo DP (s)'], 
             marker='o', linewidth=2.5, label='DP', color='blue')
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Tempo Rec (s)'], 
             marker='s', linewidth=2.5, label='Recursivo', color='red')
    
    plt.xlabel('Tamanho da String', fontsize=12, fontweight='bold')
    plt.ylabel('Tempo (segundos)', fontsize=12, fontweight='bold')
    plt.title('Comparação de Tempo: DP vs Recursivo', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "11_comparacao_tempo_dp_vs_rec.png"), dpi=300)
    print("✅ Gráfico '11_comparacao_tempo_dp_vs_rec.png' salvo")
    plt.close()


def plotar_comparacao_tempo_dp_vs_rec_limitado(df):
    """Plota comparação unificada de tempo DP vs Recursivo (primeiras 17 linhas)."""
    df_limitado = df.iloc[:17].copy()
    df_com_rec = df_limitado[df_limitado['Tempo Rec (s)'] != 'N/A'].copy()
    
    if df_com_rec.empty:
        print("⚠️ Sem dados: Comparação DP vs Rec (limitado)")
        return
    
    df_com_rec['Tempo Rec (s)'] = df_com_rec['Tempo Rec (s)'].astype(float)
    df_com_rec['Tempo DP (s)'] = df_com_rec['Tempo DP (s)'].astype(float)
    
    plt.figure(figsize=(12, 7))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Tempo DP (s)'], 
             marker='o', linewidth=2.5, label='DP', color='blue')
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Tempo Rec (s)'], 
             marker='s', linewidth=2.5, label='Recursivo', color='red')
    
    plt.xlabel('Tamanho da String', fontsize=12, fontweight='bold')
    plt.ylabel('Tempo (segundos)', fontsize=12, fontweight='bold')
    plt.title('Comparação de Tempo: DP vs Recursivo (Até Linha 17)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "11_comparacao_tempo_dp_vs_rec_limitado.png"), dpi=300)
    print("✅ Gráfico '11_comparacao_tempo_dp_vs_rec_limitado.png' salvo")
    plt.close()
    
def plotar_comparacao_memoria_dp_vs_rec_limitado(df):
    """Plota comparação de uso de memória DP vs Recursivo (primeiras 17 linhas)."""
    df_limitado = df.iloc[:17].copy()
    df_com_rec = df_limitado[df_limitado['Mem Rec Estimada (MB)'] != 'N/A'].copy()
    
    if df_com_rec.empty:
        print("⚠️ Sem dados: Comparação Memória DP vs Rec (limitado)")
        return
    
    df_com_rec['Mem Rec Estimada (MB)'] = df_com_rec['Mem Rec Estimada (MB)'].astype(float)
    df_com_rec['Mem DP (MB)'] = df_com_rec['Mem DP (MB)'].astype(float)
    
    plt.figure(figsize=(12, 7))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Mem DP (MB)'], 
             marker='o', linewidth=2.5, label='DP', color='green')
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Mem Rec Estimada (MB)'], 
             marker='s', linewidth=2.5, label='Recursivo', color='orange')
    
    plt.xlabel('Tamanho da String', fontsize=12, fontweight='bold')
    plt.ylabel('Memória (MB)', fontsize=12, fontweight='bold')
    plt.title('Comparação de Uso de Memória: DP vs Recursivo (Até Linha 17)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "12_comparacao_memoria_dp_vs_rec_limitado.png"), dpi=300)
    print("✅ Gráfico '12_comparacao_memoria_dp_vs_rec_limitado.png' salvo")
    plt.close()
    
def plotar_comparacao_memoria_dp_vs_rec(df):
    """Plota comparação de uso de memória DP vs Recursivo."""
    df_com_rec = df[df['Mem Rec Estimada (MB)'] != 'N/A'].copy()
    
    if df_com_rec.empty:
        print("⚠️ Sem dados: Comparação Memória DP vs Rec")
        return
    
    df_com_rec['Mem Rec Estimada (MB)'] = df_com_rec['Mem Rec Estimada (MB)'].astype(float)
    df_com_rec['Mem DP (MB)'] = df_com_rec['Mem DP (MB)'].astype(float)
    
    plt.figure(figsize=(12, 7))
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Mem DP (MB)'], 
             marker='o', linewidth=2.5, label='DP', color='green')
    plt.plot(df_com_rec['Tamanho'], df_com_rec['Mem Rec Estimada (MB)'], 
             marker='s', linewidth=2.5, label='Recursivo', color='orange')
    
    plt.xlabel('Tamanho da String', fontsize=12, fontweight='bold')
    plt.ylabel('Memória (MB)', fontsize=12, fontweight='bold')
    plt.title('Comparação de Uso de Memória: DP vs Recursivo', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "13_comparacao_memoria_dp_vs_rec.png"), dpi=300)
    print("✅ Gráfico '13_comparacao_memoria_dp_vs_rec.png' salvo")
    plt.close()
    
def plotar_tabela(df):
    """Plota a tabela de resultados em formato visual."""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('tight')
    ax.axis('off')
    
    # Cria a tabela
    tabela = ax.table(cellText=df.values, colLabels=df.columns, 
                      cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(9)
    tabela.scale(1, 2)
    
    # Formata o header (cabeçalho)
    for i in range(len(df.columns)):
        tabela[(0, i)].set_facecolor('#4CAF50')
        tabela[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alterna cores nas linhas
    for i in range(1, len(df) + 1):
        for j in range(len(df.columns)):
            if i % 2 == 0:
                tabela[(i, j)].set_facecolor('#f0f0f0')
            else:
                tabela[(i, j)].set_facecolor('#ffffff')
    
    plt.title('Tabela de Resultados LCS', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "14_tabela_resultados.png"), dpi=300, bbox_inches='tight')
    print("✅ Gráfico '14_tabela_resultados.png' salvo")
    plt.close()
    
def plotar_tabela(df):
    """Plota a tabela de resultados em formato visual e legível."""
    fig, ax = plt.subplots(figsize=(20, 12))
    ax.axis('tight')
    ax.axis('off')
    
    # Limita a quantidade de linhas exibidas para melhor legibilidade
    df_exibicao = df.head(20).copy()
    
    # Remove colunas de descrição e razão
    colunas_remover = [col for col in df_exibicao.columns if 'Descrição' in col or 'Razao' in col]
    df_exibicao = df_exibicao.drop(columns=colunas_remover)
    
    # Cria a tabela
    tabela = ax.table(cellText=df_exibicao.values, colLabels=df_exibicao.columns, 
                      cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.scale(1, 2.5)
    
    # Formata o header (cabeçalho)
    for i in range(len(df_exibicao.columns)):
        tabela[(0, i)].set_facecolor('#2196F3')
        tabela[(0, i)].set_text_props(weight='bold', color='white', fontsize=11)
    
    # Alterna cores nas linhas para melhor legibilidade
    for i in range(1, len(df_exibicao) + 1):
        for j in range(len(df_exibicao.columns)):
            if i % 2 == 0:
                tabela[(i, j)].set_facecolor('#E3F2FD')
            else:
                tabela[(i, j)].set_facecolor('#FFFFFF')
            tabela[(i, j)].set_text_props(fontsize=10)
    
    plt.title('Tabela de Resultados LCS (Primeiras 20 linhas)', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "14_tabela_resultados.png"), dpi=300, bbox_inches='tight')
    print("✅ Gráfico '14_tabela_resultados.png' salvo")
    plt.close()

# ========================
# EXECUÇÃO PRINCIPAL
# ========================

def plotar_todos_graficos():
    """Plota gráficos individuais para cada coluna."""
    if not os.path.exists(RESULT_FILE):
        print(f"❌ Arquivo '{RESULT_FILE}' não encontrado!")
        print("Execute 'testes_mais_completos.py' primeiro.")
        return
    
    criar_diretorio_graficos()
    print("Carregando dados...")
    df = carregar_dados()
    
    print("\nGerando gráficos individuais...\n")
    plotar_tamanho(df)
    plotar_comprimento_lcs(df)
    plotar_tempo_dp(df)
    plotar_razao_tempo_dp(df)
    plotar_memoria_dp(df)
    plotar_razao_memoria_dp(df)
    plotar_tempo_rec(df)
    plotar_memoria_rec(df)
    plotar_chamadas_rec(df)
    plotar_razao_crescimento_rec(df)
    plotar_comparacao_tempo_dp_vs_rec(df)
    plotar_comparacao_tempo_dp_vs_rec_limitado(df)
    plotar_comparacao_memoria_dp_vs_rec_limitado(df)
    plotar_comparacao_memoria_dp_vs_rec(df)
    plotar_tabela(df)
    
    print("\n✅ Todos os gráficos foram gerados com sucesso!")


def exibir_menu():
    """Exibe menu interativo para escolher gráficos."""
    print("\n" + "="*60)
    print("📊 MENU DE GRÁFICOS - LCS")
    print("="*60)
    print("1.  Tamanho da String")
    print("2.  Comprimento do LCS")
    print("3.  Tempo de Execução - DP")
    print("4.  Razão de Crescimento de Tempo - DP")
    print("5.  Uso de Memória - DP")
    print("6.  Razão de Crescimento de Memória - DP")
    print("7.  Tempo de Execução - Recursivo")
    print("8.  Uso de Memória - Recursivo")
    print("9.  Número de Chamadas Recursivas")
    print("10. Razão de Crescimento - Chamadas Recursivas")
    print("11. Comparação de Tempo: DP vs Recursivo")
    print("12. Comparação de Tempo: DP vs Recursivo (Até Linha 17)")
    print("13. Comparação de Memória: DP vs Recursivo (Até Linha 17)")
    print("14. Comparação de Memória: DP vs Recursivo")
    print("15. Tabela de Resultados")
    print("16. Plotar TODOS os gráficos")
    print("0.  Sair")
    print("="*60)


def menu_principal():
    """Menu principal para seleção de gráficos."""
    if not os.path.exists(RESULT_FILE):
        print(f"❌ Arquivo '{RESULT_FILE}' não encontrado!")
        print("Execute 'testes_mais_completos.py' primeiro.")
        return
    
    criar_diretorio_graficos()
    df = carregar_dados()
    
    while True:
        exibir_menu()
        opcao = input("\n👉 Digite a opção desejada: ").strip()
        
        print()
        
        if opcao == "1":
            plotar_tamanho(df)
        elif opcao == "2":
            plotar_comprimento_lcs(df)
        elif opcao == "3":
            plotar_tempo_dp(df)
        elif opcao == "4":
            plotar_razao_tempo_dp(df)
        elif opcao == "5":
            plotar_memoria_dp(df)
        elif opcao == "6":
            plotar_razao_memoria_dp(df)
        elif opcao == "7":
            plotar_tempo_rec(df)
        elif opcao == "8":
            plotar_memoria_rec(df)
        elif opcao == "9":
            plotar_chamadas_rec(df)
        elif opcao == "10":
            plotar_razao_crescimento_rec(df)
        elif opcao == "11":
            plotar_comparacao_tempo_dp_vs_rec(df)
        elif opcao == "12":
            plotar_comparacao_tempo_dp_vs_rec_limitado(df)
        elif opcao == "13":
            plotar_comparacao_memoria_dp_vs_rec_limitado(df)
        elif opcao == "14":
            plotar_comparacao_memoria_dp_vs_rec(df)
        elif opcao == "15":
            plotar_tabela(df)
        elif opcao == "16":
            plotar_todos_graficos()
        elif opcao == "0":
            print("👋 Encerrando programa...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\n⏳ Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu_principal()
