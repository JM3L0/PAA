import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import os
import sys

# Adiciona o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import n_rainhas_backtracking
import n_rainhas_guloso


def desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida, 
                       posicao_analisada=None, candidatos=None, 
                       escolhida=None, conflitos=None, seta_texto=None):
    """
    Desenha o tabuleiro de xadrez com as rainhas posicionadas e indicações visuais.
    
    Args:
        tabuleiro: Lista com as posições das rainhas (índice = linha, valor = coluna)
        n: Tamanho do tabuleiro
        titulo: Título da imagem
        passo: Número do passo atual
        pasta_saida: Pasta onde salvar a imagem
        posicao_analisada: Tupla (linha, coluna) da posição sendo analisada
        candidatos: Lista de colunas candidatas para destacar
        escolhida: Tupla (linha, coluna) da posição escolhida
        conflitos: Lista de tuplas (linha, coluna) em conflito
        seta_texto: Texto para exibir com seta apontando
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.set_xlim(-0.5, n + 0.5)
    ax.set_ylim(-0.5, n + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Desenha o tabuleiro
    for i in range(n):
        for j in range(n):
            cor = '#F0D9B5' if (i + j) % 2 == 0 else '#B58863'
            
            # Destaca casas candidatas em amarelo claro
            if candidatos and i < len(tabuleiro) and tabuleiro[i] == -1:
                for linha_cand in range(n):
                    if j in candidatos and linha_cand == i:
                        cor = '#FFEB99'
            
            # Destaca a posição sendo analisada em azul claro
            if posicao_analisada and posicao_analisada[0] == i and posicao_analisada[1] == j:
                cor = '#87CEEB'
            
            # Destaca a posição escolhida em verde claro
            if escolhida and escolhida[0] == i and escolhida[1] == j:
                cor = '#90EE90'
            
            # Destaca conflitos em vermelho claro
            if conflitos:
                for conf in conflitos:
                    if conf[0] == i and conf[1] == j:
                        cor = '#FFB6C6'
            
            square = patches.Rectangle((j, n - 1 - i), 1, 1, 
                                       linewidth=2, edgecolor='black', 
                                       facecolor=cor)
            ax.add_patch(square)
    
    # Desenha as rainhas já colocadas
    for i in range(n):
        if tabuleiro[i] != -1:
            # Rainha na posição (i, tabuleiro[i])
            ax.text(tabuleiro[i] + 0.5, n - 1 - i + 0.5, '♛', 
                   fontsize=70, ha='center', va='center', color='#8B0000', 
                   fontweight='bold')
    
    # Desenha seta apontando para a posição escolhida
    if escolhida:
        linha, coluna = escolhida
        arrow = FancyArrowPatch(
            (coluna + 0.5, n - 1 - linha + 1.8),
            (coluna + 0.5, n - 1 - linha + 1.15),
            arrowstyle='->,head_width=0.6,head_length=0.6',
            color='green', linewidth=4, zorder=5,
            mutation_scale=25
        )
        ax.add_patch(arrow)
        if seta_texto:
            ax.text(coluna + 0.5, n - 1 - linha + 2.4, seta_texto,
                   fontsize=14, ha='center', va='bottom', color='green',
                   fontweight='bold', bbox=dict(boxstyle='round,pad=0.5', 
                   facecolor='white', edgecolor='green', linewidth=2))
    
    # Adiciona legenda visual
    legenda_y = -0.5
    if candidatos or posicao_analisada or escolhida or conflitos:
        legenda_items = []
        legenda_x = 0
        
        if posicao_analisada:
            rect = patches.Rectangle((legenda_x, legenda_y), 0.4, 0.4, 
                                    facecolor='#87CEEB', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(legenda_x + 0.5, legenda_y + 0.2, 'Analisando', 
                   fontsize=12, va='center')
            legenda_x += 2.0
        
        if candidatos:
            rect = patches.Rectangle((legenda_x, legenda_y), 0.4, 0.4, 
                                    facecolor='#FFEB99', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(legenda_x + 0.5, legenda_y + 0.2, 'Candidatas', 
                   fontsize=12, va='center')
            legenda_x += 2.0
        
        if escolhida:
            rect = patches.Rectangle((legenda_x, legenda_y), 0.4, 0.4, 
                                    facecolor='#90EE90', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(legenda_x + 0.5, legenda_y + 0.2, 'Escolhida', 
                   fontsize=12, va='center')
            legenda_x += 2.0
        
        if conflitos:
            rect = patches.Rectangle((legenda_x, legenda_y), 0.4, 0.4, 
                                    facecolor='#FFB6C6', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(legenda_x + 0.5, legenda_y + 0.2, 'Conflito', 
                   fontsize=12, va='center')
    
    # Adiciona números de linhas e colunas
    for i in range(n):
        ax.text(-0.3, n - 1 - i + 0.5, str(i), fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(i + 0.5, n + 0.2, str(i), fontsize=12, ha='center', va='center', fontweight='bold')
    
    ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
    
    # Salva a imagem
    nome_arquivo = os.path.join(pasta_saida, f'passo_{passo:03d}.png')
    plt.savefig(nome_arquivo, bbox_inches='tight', dpi=150)
    plt.close()
    
    return nome_arquivo


def verificar_conflitos(tabuleiro, linha):
    """Retorna o número de conflitos até a linha atual."""
    conflitos = 0
    for i in range(linha):
        if tabuleiro[i] != -1:
            for j in range(i + 1, linha + 1):
                if tabuleiro[j] != -1:
                    if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                        conflitos += 1
    return conflitos


def obter_posicoes_conflito(tabuleiro, linha, coluna):
    """Retorna lista de posições em conflito com a posição (linha, coluna)."""
    conflitos = []
    for i in range(linha):
        if tabuleiro[i] != -1:
            if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
                conflitos.append((i, tabuleiro[i]))
    return conflitos


# ==================== BACKTRACKING ====================

def gerar_exemplos_backtracking(n=4):
    """Gera imagens do passo a passo do algoritmo Backtracking."""
    pasta_saida = os.path.join(os.path.dirname(__file__), 'backtracking')
    os.makedirs(pasta_saida, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Gerando exemplos do algoritmo BACKTRACKING para N={n}")
    print(f"{'='*60}\n")
    
    tabuleiro = [-1] * n
    passo = [0]  # Usar lista para modificar dentro da função recursiva
    
    def backtracking_visualizar(linha):
        if linha == n:
            # Solução encontrada
            passo[0] += 1
            titulo = f'Backtracking - Solução Encontrada!\nTabuleiro: {tabuleiro}'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida)
            print(f"Passo {passo[0]:3d}: Solução encontrada! -> {arquivo}")
            return True
        
        for coluna in range(n):
            # Visualiza análise da posição
            passo[0] += 1
            conflitos = obter_posicoes_conflito(tabuleiro, linha, coluna)
            eh_segura = len(conflitos) == 0
            
            if eh_segura:
                titulo = f'Backtracking - Passo {passo[0]}\nTestando linha {linha}, coluna {coluna}\n✓ Posição SEGURA (sem conflitos)'
                arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida,
                                            posicao_analisada=(linha, coluna))
            else:
                titulo = f'Backtracking - Passo {passo[0]}\nTestando linha {linha}, coluna {coluna}\n✗ Conflito com {len(conflitos)} rainha(s)'
                arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida,
                                            posicao_analisada=(linha, coluna),
                                            conflitos=conflitos)
            print(f"Passo {passo[0]:3d}: Testando ({linha},{coluna}) - {'Seguro' if eh_segura else f'Conflito com {len(conflitos)} rainha(s)'} -> {arquivo}")
            
            if n_rainhas_backtracking.eh_seguro(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna
                passo[0] += 1
                
                titulo = f'Backtracking - Passo {passo[0]}\n✓ Rainha colocada na linha {linha}, coluna {coluna}\nTabuleiro: {tabuleiro[:linha+1]}'
                arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida,
                                            escolhida=(linha, coluna),
                                            seta_texto='Colocada!')
                print(f"Passo {passo[0]:3d}: Colocando rainha na linha {linha}, coluna {coluna} -> {arquivo}")
                
                if backtracking_visualizar(linha + 1):
                    return True
                
                # Backtrack
                tabuleiro[linha] = -1
                passo[0] += 1
                titulo = f'Backtracking - Passo {passo[0]}\n← BACKTRACK da linha {linha}\nRemovendo rainha e tentando outra posição'
                arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida)
                print(f"Passo {passo[0]:3d}: Backtrack na linha {linha} -> {arquivo}")
        
        return False
    
    # Estado inicial
    passo[0] += 1
    titulo = f'Backtracking - Passo {passo[0]}\nEstado Inicial\nTabuleiro vazio'
    arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo[0], pasta_saida)
    print(f"Passo {passo[0]:3d}: Estado inicial -> {arquivo}")
    
    backtracking_visualizar(0)
    
    print(f"\n✓ Total de {passo[0]} imagens geradas em: {pasta_saida}\n")


# ==================== GULOSO SIMPLES ====================

def gerar_exemplos_guloso_simples(n=4):
    """Gera imagens do passo a passo do algoritmo Guloso Simples."""
    pasta_saida = os.path.join(os.path.dirname(__file__), 'guloso_simples')
    os.makedirs(pasta_saida, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Gerando exemplos do algoritmo GULOSO SIMPLES para N={n}")
    print(f"{'='*60}\n")
    
    tabuleiro = [-1] * n
    passo = 0
    
    # Estado inicial
    passo += 1
    titulo = f'Guloso Simples - Passo {passo}\nEstado Inicial\nTabuleiro vazio'
    arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida)
    print(f"Passo {passo:3d}: Estado inicial -> {arquivo}")
    
    for linha in range(n):
        menor = float('inf')
        melhor = 0
        conflitos_por_coluna = []
        
        # Primeira passagem: analisa cada coluna
        for coluna in range(n):
            conflitos = n_rainhas_guloso.contar_conflitos(tabuleiro, linha, coluna)
            conflitos_por_coluna.append(conflitos)
            
            # Visualiza análise de cada coluna
            passo += 1
            posicoes_conflito = obter_posicoes_conflito(tabuleiro, linha, coluna)
            titulo = f'Guloso Simples - Passo {passo}\nAnalisando linha {linha}, coluna {coluna}\nConflitos encontrados: {conflitos}'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida,
                                        posicao_analisada=(linha, coluna),
                                        conflitos=posicoes_conflito if conflitos > 0 else None)
            print(f"Passo {passo:3d}: Analisando ({linha},{coluna}), conflitos={conflitos} -> {arquivo}")
            
            if conflitos < menor:
                menor = conflitos
                melhor = coluna
        
        # Mostra comparação final
        passo += 1
        titulo = f'Guloso Simples - Passo {passo}\nComparação linha {linha}\nConflitos: {conflitos_por_coluna}\nMelhor escolha: coluna {melhor} (mínimo = {menor} conflitos)'
        arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida,
                                     escolhida=(linha, melhor))
        print(f"Passo {passo:3d}: Melhor opção para linha {linha}: coluna {melhor} -> {arquivo}")
        
        # Coloca a rainha
        tabuleiro[linha] = melhor
        passo += 1
        titulo = f'Guloso Simples - Passo {passo}\n✓ Rainha colocada na linha {linha}, coluna {melhor}\nTabuleiro: {tabuleiro[:linha+1]}'
        arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida,
                                    escolhida=(linha, melhor),
                                    seta_texto=f'Escolhida!\n{menor} conflitos')
        print(f"Passo {passo:3d}: Rainha colocada na linha {linha}, coluna {melhor} -> {arquivo}")
    
    # Estado final
    passo += 1
    valido = n_rainhas_guloso.eh_valido(tabuleiro)
    titulo = f'Guloso Simples - Resultado Final\nTabuleiro: {tabuleiro}\nSolução válida: {valido}'
    arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo, pasta_saida)
    print(f"Passo {passo:3d}: Resultado final (válido: {valido}) -> {arquivo}")
    
    print(f"\n✓ Total de {passo} imagens geradas em: {pasta_saida}\n")


# ==================== GULOSO COM RESTART ====================

def gerar_exemplos_guloso_restart(n=4):
    """Gera imagens do passo a passo do algoritmo Guloso com Restart."""
    pasta_saida = os.path.join(os.path.dirname(__file__), 'guloso_restart')
    os.makedirs(pasta_saida, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Gerando exemplos do algoritmo GULOSO COM RESTART para N={n}")
    print(f"{'='*60}\n")
    
    import random
    random.seed(42)  # Para reprodutibilidade
    
    tentativa = 0
    passo_global = 0
    
    max_tentativas = 10
    for tentativa in range(max_tentativas):
        print(f"\n--- Tentativa {tentativa + 1} ---")
        tabuleiro = [-1] * n
        
        # Estado inicial da tentativa
        passo_global += 1
        titulo = f'Guloso Restart - Passo {passo_global}\nTentativa {tentativa + 1} - Estado Inicial\nTabuleiro vazio'
        arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida)
        print(f"Passo {passo_global:3d}: Tentativa {tentativa + 1} - Estado inicial -> {arquivo}")
        
        for linha in range(n):
            candidatos = []
            menor = float('inf')
            conflitos_por_coluna = []
            
            # Analisa cada coluna
            for coluna in range(n):
                conflitos = n_rainhas_guloso.contar_conflitos(tabuleiro, linha, coluna)
                conflitos_por_coluna.append(conflitos)
                
                # Visualiza análise
                passo_global += 1
                posicoes_conflito = obter_posicoes_conflito(tabuleiro, linha, coluna)
                titulo = f'Guloso Restart - Passo {passo_global} (T{tentativa + 1})\nAnalisando linha {linha}, coluna {coluna}\nConflitos: {conflitos}'
                arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida,
                                            posicao_analisada=(linha, coluna),
                                            conflitos=posicoes_conflito if conflitos > 0 else None)
                print(f"Passo {passo_global:3d}: T{tentativa + 1} - Analisando ({linha},{coluna}), conflitos={conflitos} -> {arquivo}")
                
                if conflitos < menor:
                    menor = conflitos
                    candidatos = [coluna]
                elif conflitos == menor:
                    candidatos.append(coluna)
            
            # Mostra candidatos
            passo_global += 1
            titulo = f'Guloso Restart - Passo {passo_global} (T{tentativa + 1})\nLinha {linha} - Conflitos: {conflitos_por_coluna}\nCandidatos empatados (min={menor}): {candidatos}'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida,
                                        candidatos=candidatos)
            print(f"Passo {passo_global:3d}: T{tentativa + 1} - Candidatos para linha {linha}: {candidatos} -> {arquivo}")
            
            # Escolhe aleatoriamente entre os candidatos
            escolhido = random.choice(candidatos)
            
            # Mostra escolha
            passo_global += 1
            titulo = f'Guloso Restart - Passo {passo_global} (T{tentativa + 1})\nEscolha aleatória entre candidatos\nCandidatos: {candidatos} → Escolhido: {escolhido}'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida,
                                        candidatos=candidatos,
                                        escolhida=(linha, escolhido))
            print(f"Passo {passo_global:3d}: T{tentativa + 1} - Escolhido aleatoriamente: coluna {escolhido} -> {arquivo}")
            
            # Coloca a rainha
            tabuleiro[linha] = escolhido
            passo_global += 1
            titulo = f'Guloso Restart - Passo {passo_global} (T{tentativa + 1})\n✓ Rainha colocada na linha {linha}, coluna {escolhido}\nTabuleiro: {tabuleiro[:linha+1]}'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida,
                                        escolhida=(linha, escolhido),
                                        seta_texto=f'Aleatória!\n{menor} conflitos')
            print(f"Passo {passo_global:3d}: T{tentativa + 1} - Rainha na linha {linha}, coluna {escolhido} -> {arquivo}")
        
        # Verifica se é válido
        valido = n_rainhas_guloso.eh_valido(tabuleiro)
        passo_global += 1
        
        if valido:
            titulo = f'Guloso Restart - SOLUÇÃO ENCONTRADA!\nTentativa {tentativa + 1}\nTabuleiro: {tabuleiro}\nSolução válida!'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida)
            print(f"Passo {passo_global:3d}: T{tentativa + 1} - SOLUÇÃO VÁLIDA ENCONTRADA! -> {arquivo}")
            break
        else:
            titulo = f'Guloso Restart - Tentativa {tentativa + 1} Falhou\nTabuleiro: {tabuleiro}\nSolução inválida - Reiniciando...'
            arquivo = desenhar_tabuleiro(tabuleiro, n, titulo, passo_global, pasta_saida)
            print(f"Passo {passo_global:3d}: T{tentativa + 1} - Solução inválida, reiniciando... -> {arquivo}")
    
    print(f"\n✓ Total de {passo_global} imagens geradas em: {pasta_saida}\n")


# ==================== MAIN ====================

def main():
    """Executa a geração de exemplos para todos os algoritmos."""
    n = 4
    
    print("\n" + "="*60)
    print("GERADOR DE EXEMPLOS VISUAIS - N-RAINHAS")
    print(f"Tamanho do tabuleiro: {n}x{n}")
    print("="*60)
    
    # Gera exemplos para cada algoritmo
    gerar_exemplos_backtracking(n)
    gerar_exemplos_guloso_simples(n)
    gerar_exemplos_guloso_restart(n)
    
    print("\n" + "="*60)
    print("✓ TODOS OS EXEMPLOS FORAM GERADOS COM SUCESSO!")
    print("="*60)
    print("\nPastas criadas:")
    print("  - exemplos/backtracking/")
    print("  - exemplos/guloso_simples/")
    print("  - exemplos/guloso_restart/")
    print("\n")


if __name__ == "__main__":
    main()
