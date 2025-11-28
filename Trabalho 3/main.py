import n_rainhas_backtracking
import n_rainhas_guloso
import resul_salvos.plotar_graficos as pg

def pegar_entrada():
    n = int(input("Digite o tamanho do tabuleiro (N): "))
    return n

def menu():
    print("=== N-Rainhas ===")
    print("1. Executar algoritmo Guloso Simples")
    print("2. Executar algoritmo Guloso com Restart")
    print("3. Executar algoritmo Backtracking")
    print("4. Executar teste comparativo entre os algoritmos")
    print("5. Plotar graficos dos resultados salvos")
    print("0. Sair")
    escolha = input("Escolha uma opcao: ")
    
    if escolha == '1':
        n = pegar_entrada()
        tabuleiro = n_rainhas_guloso.n_rainhas_guloso_simples(n)
        print(f"Solucao Guloso Simples: {tabuleiro}")
        print(f"Valida: {n_rainhas_guloso.eh_valido(tabuleiro)}")
    elif escolha == '2':
        n = pegar_entrada()
        tabuleiro = n_rainhas_guloso.n_rainhas_guloso_com_restart(n)
        print(f"Solucao Guloso com Restart: {tabuleiro}")
        print(f"Valida: {n_rainhas_guloso.eh_valido(tabuleiro)}")
    elif escolha == '3':
        n = pegar_entrada()
        solucoes = n_rainhas_backtracking.n_rainhas_backtracking(n)
        print(f"Numero de solucoes Backtracking: {len(solucoes)}")
        if solucoes:
            print(f"Primeira solucao: {solucoes[0]}")
    elif escolha == '4':
        import resultados.teste_BT_vs_Guloso as teste
        teste.executar_testes()
    elif escolha == '5':
        pg.main()
    elif escolha == '0':
        print("Saindo...")

def main():
    while True:
        menu()
        continuar = input("Deseja realizar outra operacao? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
