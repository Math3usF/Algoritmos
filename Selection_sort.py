"""
    Selection Sort (Ordenação por Seleção)
    Estratégia: Varre a lista em busca do menor valor e o coloca na primeira 
    posição disponível. Repete o processo para o restante da lista.
    Eficiência: Lento, faz muitas comparações. Complexidade: O(n^2).
"""

def selection_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    for i in range(n):
        indice_minimo = i
        # Procura o menor elemento no restante da lista
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[indice_minimo]:
                indice_minimo = j
        # Troca o menor elemento encontrado com o elemento da posição atual
        lista_copia[i], lista_copia[indice_minimo] = lista_copia[indice_minimo], lista_copia[i]
    return lista_copia