from scr.utils import medir_tempo
from scr.inserction import insertion_sort
from scr.inserctionBinary import binary_insertion_sort
from gerador_de_entradas.gerrador import gerar_entradas

def main():
    # Gerar entradas
    gerar_entradas(tamanho_base=10000)
    
    # Número de repetições definido em UM único lugar
    repeticoes = 30
    
    # Lista automática dos arquivos
    arquivos = [f"Trabalho 1/entradas/{tipo}_{n}.txt"
                for tipo in ["crescente", "decrescente", "aleatorio"]
                for n in [1, 2, 4]]

    print("\n" + "=" * 80)
    print("TESTES COM INSERTION SORT")
    print("=" * 80)
    medir_tempo(arquivos, insertion_sort, "tempos_insertion_sort.txt", repeticoes=repeticoes)

    print("\n" + "=" * 80)
    print("TESTES COM BINARY INSERTION SORT")
    print("=" * 80)
    medir_tempo(arquivos, binary_insertion_sort, "tempos_binary_insertion_sort.txt", repeticoes=repeticoes)

if __name__ == "__main__":
    main()
