def eh_seguro(tabuleiro, linha, coluna):
    for i in range(linha):
        if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    return True

def backtracking_rec(tabuleiro, linha, n, solucoes):
    if linha == n:
        solucoes.append(tabuleiro[:])
        return
    for coluna in range(n):
        if eh_seguro(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            backtracking_rec(tabuleiro, linha + 1, n, solucoes)

def n_rainhas_backtracking(n):
    tabuleiro = [-1] * n
    solucoes = []
    backtracking_rec(tabuleiro, 0, n, solucoes)
    return solucoes
