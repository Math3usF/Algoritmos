"""
    Radix Sort (Ordenação por Raiz/Dígito)
    Estratégia: Ordena os números processando dígito por dígito, começando pela 
    unidade até a maior casa decimal. Usa o Counting Sort internamente.
    Eficiência: Ótimo para listas de números grandes. Complexidade: O(d(n + k)).
"""

def counting_sort_para_radix(lista, casa_decimal): #Função de contagem adaptada para o Radix Sort, ordena os números com base no dígito específico (casa decimal)
    tamanho = len(lista)
    resultado = [0] * tamanho
    contagem = [0] * 10 # Base 10 (dígitos de 0 a 9)
    
    for i in range(tamanho):
        indice = lista[i] // casa_decimal
        contagem[indice % 10] += 1
        
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
        
    for i in range(tamanho - 1, -1, -1):
        indice = lista[i] // casa_decimal
        resultado[contagem[indice % 10] - 1] = lista[i]
        contagem[indice % 10] -= 1
        
    for i in range(tamanho):
        lista[i] = resultado[i]

def radix_sort(lista):
    if not lista:
        return []
    lista_copia = lista.copy()
    valor_maximo = max(lista_copia)
    
    # Faz a ordenação para cada casa decimal (1, 10, 100...)
    casa_decimal = 1
    while valor_maximo // casa_decimal > 0:
        counting_sort_para_radix(lista_copia, casa_decimal)
        casa_decimal *= 10
        
    return lista_copia
