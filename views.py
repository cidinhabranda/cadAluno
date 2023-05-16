import sys
# Trabalhando com lista -----------------------------------
# ver dados
todos_dados = []
def ver_dados():
    return todos_dados
    # print(todos_dados)
# funcao adicionar item na lista
def adicionar_dados(i):
    todos_dados.append(i)
# funcao remover da lista
def remover_dados(ra):
    valor_procurado = ra
    # iterando sobre cada elemento da lista
    for elemento in todos_dados:
        # verificando se o valor está presente no elemento
        if valor_procurado in elemento:
            # removendo o elemento que contém o valor
            todos_dados.remove(elemento)
    #print(todos_dados)

# funcao atualizar
def atualizar_dados(i):
    valor_procurado = i[0]
    # iterando sobre cada elemento da lista
    for elemento in todos_dados:
        # verificando se o valor está presente no elemento
        if valor_procurado in elemento:
            # encontrando o índice da posição onde o email está armazenado
            # indice = elemento.index(valor_procurado)
            # atualizando o email do elemento
            elemento[0] = i[1]
            elemento[1] = i[2]
            elemento[2] = i[3]
            elemento[3] = i[4]

# funcao procurar na lista
def procurar_dados(i):
    elemento_procurado = i
    resultados = []
    for sublista in todos_dados:
        if elemento_procurado in sublista:
            resultados.append(sublista)
    print(resultados)
    return resultados
