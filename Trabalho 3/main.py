import n_rainhas_backtracking
import n_rainhas_guloso

def pegar_entrada():
    n = int(input("Digite o tamanho do tabuleiro (N): "))
    return n

def main():
    n = pegar_entrada()
    
    # print(f"\n=== Backtracking ===")
    # solucoes = n_rainhas_backtracking.n_rainhas_backtracking(n)
    # print(f"Numero de solucoes: {len(solucoes)}")
    # if solucoes:
    #     print(f"Primeira solucao: {solucoes[0]}")
    
    print(f"\n=== Guloso Simples ===")
    tabuleiro_simples = n_rainhas_guloso.n_rainhas_guloso_simples(n)
    print(f"Solucao: {tabuleiro_simples}")
    print(f"Valida: {n_rainhas_guloso.eh_valido(tabuleiro_simples)}")
    
    print(f"\n=== Guloso com Restart ===")
    tabuleiro_restart = n_rainhas_guloso.n_rainhas_guloso_com_restart(n)
    print(f"Solucao: {tabuleiro_restart}")
    print(f"Valida: {n_rainhas_guloso.eh_valido(tabuleiro_restart)}")

if __name__ == "__main__":
    main()
