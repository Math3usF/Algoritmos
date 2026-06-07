"""
    Bucket Sort (Ordenação por Baldes)
    Estratégia: Distribui os elementos em vários 'baldes' ou grupos. Cada balde é 
    ordenado individualmente e depois todos são juntados.
    Eficiência: Muito bom quando os dados estão bem distribuídos. Complexidade: O(n + k).
"""

def bucket_sort(lista):
    if not lista:
        return []
        
    lista_copia = lista.copy()
    valor_maximo = max(lista_copia)
    tamanho = len(lista_copia)
    
    # 1. Criando os baldes vazios
    baldes = [[] for _ in range(tamanho)]
    
    # 2. Inserindo os elementos nos baldes apropriados
    for i in range(tamanho):
        indice = int(lista_copia[i] * tamanho / (valor_maximo + 1))
        baldes[indice].append(lista_copia[i])
        
    # 3. Ordenando cada balde internamente e juntando o resultado
    resultado = []
    for balde in baldes:
        balde.sort() # Internamente usa o Timsort do Python
        resultado.extend(balde)
        
    return resultado
