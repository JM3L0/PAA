# =============================================================
# N RAINHAS - Versão reduzida
# Backtracking, Guloso 1 e Guloso 2
# =============================================================

def seguro(tab, lin, col):
    for i in range(lin):
        if tab[i] == col or abs(tab[i] - col) == abs(i - lin):
            return False
    return True


# ---------------- BACKTRACKING ----------------

def backtracking_rec(tab, lin, n):
    if lin == n:
        return True
    for col in range(n):
        if seguro(tab, lin, col):
            tab[lin] = col
            if backtracking_rec(tab, lin + 1, n):
                return True
            tab[lin] = -1
    return False

def n_rainhas_backtracking(n):
    tab = [-1] * n
    return tab if backtracking_rec(tab, 0, n) else None


# ---------------- GULOSO 1 ----------------
# Escolhe sempre a 1ª coluna possível

def n_rainhas_guloso1(n):
    tab = [-1] * n
    for lin in range(n):
        for col in range(n):
            if seguro(tab, lin, col):
                tab[lin] = col
                break
        if tab[lin] == -1:
            return None
    return tab


# ---------------- GULOSO 2 ----------------
# Escolhe a coluna com menor número de conflitos

def conflitos(tab, lin, col):
    return sum(tab[i] == col or abs(tab[i]-col) == abs(i-lin) for i in range(lin))

def n_rainhas_guloso2(n):
    tab = [-1] * n
    for lin in range(n):
        col_melhor = min(range(n), key=lambda c: conflitos(tab, lin, c))
        tab[lin] = col_melhor
    # Verifica se ficou válido
    for i in range(n):
        if not seguro(tab, i, tab[i]):
            return None
    return tab


# ---------------- Teste rápido ----------------
if __name__ == "__main__":
    n = 8
    print("Backtracking:", n_rainhas_backtracking(n))
    print("Guloso 1:", n_rainhas_guloso1(n))
    print("Guloso 2:", n_rainhas_guloso2(n))
