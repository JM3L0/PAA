def lcs_dp(X, Y):
    """
    Calcula o comprimento da LCS de X e Y usando Programação Dinâmica (bottom-up).
    """
    m = len(X)
    n = len(Y)
    
    # Criar uma tabela (c no pseudocódigo) para armazenar os comprimentos das LCS
    # A tabela tem (m+1) x (n+1) para acomodar a linha/coluna 0 (casos base).
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Preencher a tabela L de forma bottom-up (de i=1 a m e j=1 a n)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # Se x_i == y_j
            if X[i-1] == Y[j-1]:
                # L[i, j] = L[i-1, j-1] + 1 [cite: 59]
                L[i][j] = L[i-1][j-1] + 1
            
            # Se x_i != y_j
            else:
                # L[i, j] = max(L[i-1, j], L[i, j-1]) [cite: 61]
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    # O resultado final é o comprimento no canto inferior direito da tabela.
    return L[m][n]
