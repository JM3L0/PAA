def contar_conflitos(tabuleiro, linha, coluna):
    conflitos = 0
    for i in range(linha):
        if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
            conflitos += 1
    return conflitos

def n_rainhas_guloso(n):
    tabuleiro = [-1] * n
    for linha in range(n):
        menor = float('inf')
        melhor = 0
        for coluna in range(n):
            conflitos = contar_conflitos(tabuleiro, linha, coluna)
            if conflitos < menor:
                menor = conflitos
                melhor = coluna
        tabuleiro[linha] = melhor
    return tabuleiro

def eh_valido(tabuleiro):
    n = len(tabuleiro)
    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                return False
    return True
