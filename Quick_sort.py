"""
    Quick Sort (Ordenação Rápida)
    Estratégia: 'Divide e Conquista'. Escolhe um elemento como 'pivô' e divide a 
    lista em três partes: menores, iguais e maiores que o pivô.
    Eficiência: Muito rápido na maioria dos casos. Complexidade média: O(n log n)
"""

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

