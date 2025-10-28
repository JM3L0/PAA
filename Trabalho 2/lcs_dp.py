from collections import deque

def lcs_dp(X, Y):

    m = len(X)
    n = len(Y)
    
    # Criar a tabela L (comprimentos)
    # Inicializa a tabela com zeros
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Preencher a tabela L
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    return L

def lcs_reconstroi_string(X, Y, L):

    i = len(X)
    j = len(Y)

    lcs_result = deque()

    while i > 0 and j > 0:
        
        if X[i-1] == Y[j-1]:
            lcs_result.appendleft(X[i-1])
            i -= 1
            j -= 1
        
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
            
        else:
            j -= 1
    
    return "".join(lcs_result)

def printar_tabela(L):
    for row in L:
        print("\t".join(map(str, row)))