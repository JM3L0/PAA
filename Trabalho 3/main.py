import n_rainhas_backtracking
import n_rainhas_guloso

def pegar_entrada():
    n = int(input("Digite o tamanho do tabuleiro (N): "))
    return n

def main():
    n = pegar_entrada()
    
    print(f"\n=== Backtracking ===")
    solucoes = n_rainhas_backtracking.n_rainhas_backtracking(n)
    print(f"Numero de solucoes: {len(solucoes)}")
    if solucoes:
        print(f"Primeira solucao: {solucoes[0]}")
    
    print(f"\n=== Guloso ===")
    tabuleiro = n_rainhas_guloso.n_rainhas_guloso(n)
    print(f"Solucao: {tabuleiro}")
    print(f"Valida: {n_rainhas_guloso.eh_valido(tabuleiro)}")

if __name__ == "__main__":
    main()
