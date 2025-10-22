import lcs_dp
import lcs_recursive

def pegar_entrada():
    X = input("Digite a primeira sequência: ")
    Y = input("Digite a segunda sequência: ")
    return X, Y

def main():
    X, Y = pegar_entrada()
    print(f"Comprimento da LCS (DP): {lcs_dp.lcs_dp(X, Y)}")
    print(f"Comprimento da LCS (recursiva): {lcs_recursive.lcs_recursive(X, Y, len(X), len(Y))}")

if __name__ == "__main__":
    main()