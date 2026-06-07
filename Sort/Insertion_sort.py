"""
    Insertion Sort (Ordenação por Inserção)
    Estratégia: Pega um elemento de cada vez e o insere na posição correta entre 
    os elementos que já foram ordenados (como organizar cartas na mão).
    Eficiência: Lento para listas grandes, mas ótimo para listas quase ordenadas. Complexidade: O(n^2).
"""

def insertion_sort(lista):
    lista_copia = lista.copy()
    for i in range(1, len(lista_copia)):
        chave = lista_copia[i]
        j = i - 1
        # Move os elementos que são maiores que a chave para uma posição à frente
        while j >= 0 and chave < lista_copia[j]:
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = chave
    return lista_copia
