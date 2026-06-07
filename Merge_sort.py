"""
    Merge Sort (Ordenação por Mistura)
    Estratégia: 'Divide e Conquista'. Divide a lista pela metade repetidamente até 
    ter elementos únicos, depois 'mistura' (merge) essas metades em ordem.
    Eficiência: Muito consistente e seguro. Complexidade: O(n log n).
"""

def merge_sort(lista):
    # Caso base: listas com 0 ou 1 elementos já estão ordenadas
    if len(lista) <= 1:
        return lista
    
    # Dividindo a lista ao meio
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    # Misturando as metades ordenadas
    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Compara os elementos das duas listas e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            
    # Adiciona qualquer elemento que tenha sobrado
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado