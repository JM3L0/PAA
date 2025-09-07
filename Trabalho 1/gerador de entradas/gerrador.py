import random
import os

def gerar_numeros_e_salvar(inicio, quantidade, modo, nome_arquivo="numeros.txt"):
    numeros = []

    fim = inicio + quantidade - 1  # Define o fim com base na quantidade

    # Gerar a sequência conforme o modo escolhido
    if modo == "crescente":
        numeros = list(range(inicio, fim + 1))
    elif modo == "decrescente":
        numeros = list(range(fim, inicio - 1, -1))
    elif modo == "aleatorio":
        numeros = list(range(inicio, fim + 1))
        random.shuffle(numeros)
    else:
        print("Modo inválido. Use 'crescente', 'decrescente' ou 'aleatorio'.")
        return

    # Garantir que a pasta existe
    pasta = os.path.dirname(nome_arquivo)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)

    # Salvar a sequência no arquivo
    try:
        with open(nome_arquivo, "w") as arquivo:
            for numero in numeros:
                arquivo.write(f"{numero}\n")
        print(f"Números gerados e salvos em '{nome_arquivo}' ({modo}, quantidade={quantidade}).")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

# --- EXEMPLO DE USO ---
primeira_quantidade = int(input("Digite a quantidade base de números: "))
modos = ["crescente", "decrescente", "aleatorio"]

for modo in modos:
    gerar_numeros_e_salvar(1, primeira_quantidade, modo, f"Trabalho 1/entradas/{modo}_1.txt")
    gerar_numeros_e_salvar(1, primeira_quantidade * 2, modo, f"Trabalho 1/entradas/{modo}_2.txt")
    gerar_numeros_e_salvar(1, primeira_quantidade * 4, modo, f"Trabalho 1/entradas/{modo}_4.txt")
