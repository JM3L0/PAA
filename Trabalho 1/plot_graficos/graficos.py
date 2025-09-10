import matplotlib.pyplot as plt
import pandas as pd
import os

def carregar_dados():
    """Carrega os arquivos CSV da pasta dados_gf"""
    pasta = os.path.join(os.path.dirname(__file__), 'dados_gf')
    dados = {}
    
    for arquivo in ['tempos_binary_insertion_sort_agrupado.csv', 'tempos_insertion_sort_agrupado.csv']:
        caminho = os.path.join(pasta, arquivo)
        if os.path.exists(caminho):
            dados[arquivo] = pd.read_csv(caminho)
            print(f"✓ {arquivo} carregado")
    
    return dados

def encontrar_coluna(df, tipo):
    """Encontra coluna por tipo de entrada"""
    if tipo in df.columns:
        return tipo
    
    colunas = [col for col in df.columns if tipo in col.lower()]
    if not colunas and tipo == 'aleatorio':
        colunas = [col for col in df.columns if any(var in col.lower() for var in ['aleatorio', 'aleatório', 'random'])]
    
    return colunas[0] if colunas else None

def plotar(dados, tipo_algo):
    """Plota gráfico do algoritmo escolhido"""
    # Encontra dados do algoritmo
    df, nome = None, ""
    for arquivo, data in dados.items():
        is_binary = 'binary' in arquivo.lower()
        if (tipo_algo == "binary" and is_binary) or (tipo_algo == "insertion" and not is_binary):
            df, nome = data, "Binary Insertion Sort" if is_binary else "Insertion Sort"
            break
    
    if df is None:
        print(f"Dados para {tipo_algo} não encontrados!")
        return
    
    # Debug: Mostra informações do DataFrame
    print(f"\nInformações do DataFrame para {nome}:")
    print(f"Colunas: {list(df.columns)}")
    print(f"Primeiras linhas:\n{df.head()}")
    
    # Configuração do gráfico
    plt.figure(figsize=(12, 8))
    
    # Verifica se existe coluna 'tamanho' ou similar
    coluna_tamanho = None
    for col in df.columns:
        if 'tamanho' in col.lower() or 'size' in col.lower() or 'n' == col.lower():
            coluna_tamanho = col
            break
    
    if coluna_tamanho:
        tamanhos = df[coluna_tamanho]
        print(f"Usando coluna '{coluna_tamanho}' para tamanhos: {list(tamanhos)}")
    else:
        tamanhos = df.index
        print(f"Usando índices como tamanhos: {list(tamanhos)}")
    
    # Plota cada tipo de entrada
    tipos_cores = [('crescente', 'green'), ('decrescente', 'red'), ('aleatorio', 'blue')]
    for tipo, cor in tipos_cores:
        coluna = encontrar_coluna(df, tipo)
        if coluna:
            print(f"Plotando {tipo} usando coluna '{coluna}'")
            plt.plot(tamanhos, df[coluna], marker='o', linewidth=3, markersize=6, 
                    label=f'Entrada {tipo.capitalize()}', color=cor)
        else:
            print(f"Coluna para {tipo} não encontrada")
    
    # Configurações
    plt.xlabel('Tamanho da Entrada', fontsize=12)
    plt.ylabel('Tempo (s)', fontsize=12)
    plt.title(f'Análise de Performance - {nome}', fontsize=16)
    plt.grid(True, alpha=0.7, linestyle='-', linewidth=0.8, color='black')
    plt.legend(fontsize=12)
    
    if plt.gca().get_ylim()[1] > 1000:
        plt.yscale('log')
    
    plt.tight_layout()
    plt.show()

def main():
    """Função principal"""
    dados = carregar_dados()
    if not dados:
        print("Nenhum arquivo encontrado!")
        return
    
    opcoes = {"1": "insertion", "2": "binary"}
    
    while True:
        print("\n" + "="*50)
        print("GERADOR DE GRÁFICOS - ALGORITMOS DE ORDENAÇÃO")
        print("="*50)
        print("1. Insertion Sort\n2. Binary Insertion Sort\n3. Sair")
        print("-"*50)
        
        try:
            escolha = input("Digite sua opção (1, 2 ou 3): ").strip()
            
            if escolha == "3":
                print("Saindo...")
                break
            elif escolha in opcoes:
                plotar(dados, opcoes[escolha])
                if input("\nGerar outro gráfico? (s/n): ").strip().lower() not in ['s', 'sim', 'y', 'yes']:
                    print("Saindo...")
                    break
            else:
                print("Opção inválida! Digite 1, 2 ou 3.")
        except KeyboardInterrupt:
            print("\nSaindo...")
            break

if __name__ == "__main__":
    main()