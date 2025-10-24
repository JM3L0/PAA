cont_calls = 0  # Contador de chamadas recursivas
max_depth = 0   # Profundidade máxima da recursão

def lcs_recursive(X, Y, m, n, depth=1):  # Adicionamos o parâmetro 'depth'
    """Versão recursiva da LCS que retorna a string e mede chamadas e profundidade."""
    global cont_calls, max_depth
    cont_calls += 1
    max_depth = max(max_depth, depth)  # Atualiza a profundidade máxima real

    # Caso base
    if m == 0 or n == 0:
        return ""

    # Se os últimos caracteres forem iguais
    if X[m - 1] == Y[n - 1]:
        return lcs_recursive(X, Y, m - 1, n - 1, depth + 1) + X[m - 1]

    # Se forem diferentes, escolher o maior resultado
    lcs1 = lcs_recursive(X, Y, m, n - 1, depth + 1)
    lcs2 = lcs_recursive(X, Y, m - 1, n, depth + 1)
    return lcs1 if len(lcs1) > len(lcs2) else lcs2
