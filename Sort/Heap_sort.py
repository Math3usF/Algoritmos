"""
    Heap Sort (Ordenação por Monte)
    Estratégia: Transforma a lista em uma árvore binária (Max Heap) onde o maior 
    elemento fica no topo. Remove o topo e repete o processo.
    Eficiência: Excelente gerenciamento de memória. Complexidade: O(n log n).
"""


def heapify(lista, n, i): #Função para manter a propriedade do Max Heap, arvore binária onde cada nó é maior ou igual aos seus filhos
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica se o filho da esquerda é maior que a raiz
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica se o filho da direita é maior que o maior até agora
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se o maior não for a raiz, faz a troca e continua o processo
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista): #Função principal do Heap Sort
    lista_copia = lista.copy()
    n = len(lista_copia)

    # Constrói o Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista_copia, n, i)

    # Extrai os elementos um por um
    for i in range(n - 1, 0, -1):
        lista_copia[i], lista_copia[0] = lista_copia[0], lista_copia[i] # Troca
        heapify(lista_copia, i, 0)
        
    return lista_copia
