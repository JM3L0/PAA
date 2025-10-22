def lcs_recursive(X, Y, m, n):
    """
    Calcula o comprimento da LCS dos prefixos X[1..m] e Y[1..n] de forma recursiva.
    """
    # Caso base: Se um dos prefixos for vazio, a LCS tem comprimento 0.
    if m == 0 or n == 0:
        return 0
    
    # Se os últimos caracteres dos prefixos forem iguais (x_m == y_n)
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    
    # Se os últimos caracteres forem diferentes (x_m != y_n)
    # O comprimento é o máximo entre os dois subproblemas.
    else:
        return max(lcs_recursive(X, Y, m, n-1), lcs_recursive(X, Y, m-1, n))
