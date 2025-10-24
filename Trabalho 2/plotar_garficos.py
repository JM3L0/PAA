import matplotlib.pyplot as plt
import pandas as pd
import os

RESULT_FILE = os.path.join(os.path.dirname(__file__), "resultados", "tabela_de_resultados_lcs.csv")
GRAFICOS_DIR = os.path.join(os.path.dirname(__file__), "resultados")


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
    
    print("\n✅ Todos os gráficos foram gerados com sucesso!")


if __name__ == "__main__":
    plotar_todos_graficos()