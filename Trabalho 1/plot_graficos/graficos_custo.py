import matplotlib.pyplot as plt
import math

# Função para calcular o custo UNIFICADO (comparações + atribuições) do Insertion Sort
def insertion_sort_cost(n):
    # Melhor caso: 2 comparações (j >= 0, arr[j] > chave) + 3 atribuições (chave, j, arr[j+1]) por iteração
    best_case = 2 * (n - 1) + 3 * (n - 1)  # 2(n-1) comp. + 3(n-1) atrib.
    # Pior caso: 2i comp. (j >= 0, arr[j] > chave) + (2i + 3) atrib. (chave, j, arr[j+1]=arr[j], j-=1, arr[j+1]=chave)
    worst_comparisons = sum(2 * i for i in range(1, n))  # 2 * n(n-1)/2
    worst_assignments = sum(2 * i + 3 for i in range(1, n))  # 2 * n(n-1)/2 + 3(n-1)
    worst_case = worst_comparisons + worst_assignments
    return best_case, worst_case

# Função para calcular o custo UNIFICADO (comparações + atribuições) do Binary Insertion Sort
def binary_insertion_sort_cost(n):
    # Comparações na busca binária: 2 * ⌈log₂(i)⌉ por iteração (start < end, arr[mid] < chave)
    comparisons = sum(2 * math.ceil(math.log2(i)) for i in range(1, n))
    # Melhor caso: 2⌈log₂(i)⌉ atrib. (mid, start/end) + 2 atrib. (chave, pos) + 1 atrib. (arr[pos]=chave)
    best_case = comparisons + sum(2 * math.ceil(math.log2(i)) + 3 for i in range(1, n))
    # Pior caso: + i atrib. (deslocamentos) por iteração
    worst_case = comparisons + sum(2 * math.ceil(math.log2(i)) + i + 3 for i in range(1, n))
    return best_case, worst_case

# Dados para os gráficos
def generate_data():
    n_values = list(range(1, 1001))  # Tamanhos de 1 a 1000
    insertion_best = []
    insertion_worst = []
    binary_best = []
    binary_worst = []
    for n in n_values:
        best_ins, worst_ins = insertion_sort_cost(n)
        best_bin, worst_bin = binary_insertion_sort_cost(n)
        insertion_best.append(best_ins)
        insertion_worst.append(worst_ins)
        binary_best.append(best_bin)
        binary_worst.append(worst_bin)
    return n_values, insertion_best, insertion_worst, binary_best, binary_worst

# Função para plotar ambos os gráficos
def plot_both(n_values, insertion_best, insertion_worst, binary_best, binary_worst):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    # Insertion Sort
    ax1.plot(n_values, insertion_best, label="Melhor Caso (Ω(n))", color="green")
    ax1.plot(n_values, insertion_worst, label="Pior Caso (O(n²))", color="red")
    ax1.set_title("Insertion Sort: Custo Total (Comparações + Atribuições)")
    ax1.set_xlabel("Tamanho do Array (n)")
    ax1.set_ylabel("Número de Operações")
    ax1.legend()
    ax1.grid(True)
    # Binary Insertion Sort
    ax2.plot(n_values, binary_best, label="Melhor Caso (Ω(n log n))", color="green")
    ax2.plot(n_values, binary_worst, label="Pior Caso (O(n²))", color="red")
    ax2.set_title("Binary Insertion Sort: Custo Total (Comparações + Atribuições)")
    ax2.set_xlabel("Tamanho do Array (n)")
    ax2.set_ylabel("Número de Operações")
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.show()

# Função para plotar apenas Insertion Sort
def plot_insertion(n_values, insertion_best, insertion_worst):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(n_values, insertion_best, label="Melhor Caso (Ω(n))", color="green")
    ax.plot(n_values, insertion_worst, label="Pior Caso (O(n²))", color="red")
    ax.set_title("Insertion Sort: Custo Total (Comparações + Atribuições)")
    ax.set_xlabel("Tamanho do Array (n)")
    ax.set_ylabel("Número de Operações")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

# Função para plotar apenas Binary Insertion Sort
def plot_binary(n_values, binary_best, binary_worst):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(n_values, binary_best, label="Melhor Caso (Ω(n log n))", color="green")
    ax.plot(n_values, binary_worst, label="Pior Caso (O(n²))", color="red")
    ax.set_title("Binary Insertion Sort: Custo Total (Comparações + Atribuições)")
    ax.set_xlabel("Tamanho do Array (n)")
    ax.set_ylabel("Número de Operações")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

# Menu interativo
def main():
    n_values, insertion_best, insertion_worst, binary_best, binary_worst = generate_data()
    while True:
        print("\nMenu de Geração de Gráficos:")
        print("1. Gerar imagem com ambos os gráficos (Insertion e Binary Insertion Sort)")
        print("2. Gerar imagem apenas do Insertion Sort")
        print("3. Gerar imagem apenas do Binary Insertion Sort")
        print("4. Sair")
        choice = input("Escolha uma opção (1-4): ")
        
        if choice == "1":
            print("Gerando ambos os gráficos...")
            plot_both(n_values, insertion_best, insertion_worst, binary_best, binary_worst)
        elif choice == "2":
            print("Gerando gráfico do Insertion Sort...")
            plot_insertion(n_values, insertion_best, insertion_worst)
        elif choice == "3":
            print("Gerando gráfico do Binary Insertion Sort...")
            plot_binary(n_values, binary_best, binary_worst)
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()