from collections import deque

def lcs_dp(X, Y):
    """
    Calcula o comprimento da LCS de X e Y usando Programação Dinâmica (bottom-up)
    e retorna a tabela completa de comprimentos (L).
    """
    m = len(X)
    n = len(Y)
    
    # Criar a tabela L (comprimentos)
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Preencher a tabela L
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            if X[i-1] == Y[j-1]:
                # L[i, j] = L[i-1, j-1] + 1 
                L[i][j] = L[i-1][j-1] + 1
            else:
                # L[i, j] = max(L[i-1, j], L[i, j-1])
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
                
    # Retorna a tabela COMPLETA, necessária para a reconstrução
    return L

def lcs_reconstroi_string(X, Y, L):
    """
    Reconstrói a subsequência comum mais longa (LCS) a partir da tabela L.
    
    Args:
        X: primeira string
        Y: segunda string
        L: tabela de comprimentos retornada por lcs_dp_retorna_tabela
    
    Returns:
        string com a LCS reconstruída
    """
    i = len(X)
    j = len(Y)

    lcs_result = deque()

    # Percorre a tabela L de trás para frente
    while i > 0 and j > 0:
        
        # Se os caracteres casam, é um elemento da LCS
        if X[i-1] == Y[j-1]:
            lcs_result.appendleft(X[i-1])
            i -= 1
            j -= 1
        
        # Se o valor de cima é maior, move para cima
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        
        # Caso contrário, move para a esquerda
        else:
            j -= 1
    
    # A string foi construída em ordem inversa, então inverte
    return "".join(reversed(lcs_result))

def printar_tabela(L):
    """
    Função auxiliar para imprimir a tabela L de forma legível.
    """
    for row in L:
        print("\t".join(map(str, row)))