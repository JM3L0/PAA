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


# def lcs_recursive(X, Y, m, n): #aqui é para retornar a string da LCS, tenho que ver se é nescessario retornar a string ou só o tamanho
#     """
#     Calcula a LCS dos prefixos X[1..m] e Y[1..n] de forma recursiva.
#     Retorna a string da LCS encontrada.
#     """
#     # Caso base: Se um dos prefixos for vazio, a LCS é vazia.
#     if m == 0 or n == 0:
#         return ""
    
#     # Se os últimos caracteres dos prefixos forem iguais
#     elif X[m-1] == Y[n-1]:
#         return lcs_recursive(X, Y, m-1, n-1) + X[m-1]
    
#     # Se os últimos caracteres forem diferentes
#     # Retorna a maior LCS entre os dois subproblemas
#     else:
#         lcs1 = lcs_recursive(X, Y, m, n-1)
#         lcs2 = lcs_recursive(X, Y, m-1, n)
#         return lcs1 if len(lcs1) > len(lcs2) else lcs2