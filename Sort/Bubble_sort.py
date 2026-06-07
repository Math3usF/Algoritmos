"""
    Bubble Sort (Ordenação por Bolha)
    Estratégia: Compara pares vizinhos e os troca de lugar se estiverem na ordem 
    errada, 'flutuando' os maiores valores para o final da lista.
    Eficiência: Muito lento para listas grandes. Complexidade: O(n^2).
"""

def bubble_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    for i in range(n):
        # O -i-1 garante que não vamos verificar os elementos que já "flutuaram" para o final
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                # Troca os elementos de lugar
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia
