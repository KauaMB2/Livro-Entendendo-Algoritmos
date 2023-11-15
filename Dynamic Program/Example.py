def mochila_01(valor, peso, capacidade):
    n = len(valor)
    # Inicializa a tabela de programação dinâmica
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenche a tabela usando a abordagem bottom-up
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if peso[i - 1] <= w:
                tabela[i][w] = max(valor[i - 1] + tabela[i - 1][w - peso[i - 1]], tabela[i - 1][w])
            else:
                tabela[i][w] = tabela[i - 1][w]

    # Reconstrói a solução a partir da tabela
    itens_escolhidos = []
    i, w = n, capacidade
    while i > 0 and w > 0:
        if tabela[i][w] != tabela[i - 1][w]:
            itens_escolhidos.append(i - 1)
            w -= peso[i - 1]
        i -= 1

    # Retorna o valor máximo e os índices dos itens escolhidos
    return tabela[n][capacidade], itens_escolhidos

# Exemplo de uso
valor = [100, 300, 200]  # Valor associado a cada item (rádio, notebook, violão)
peso = [3, 2, 5]         # Peso de cada item
capacidade_mochila = 5  # Capacidade máxima da mochila

valor_maximo, itens_escolhidos = mochila_01(valor, peso, capacidade_mochila)

print("Valor máximo que pode ser obtido:", valor_maximo)
print("Itens escolhidos:", itens_escolhidos)
