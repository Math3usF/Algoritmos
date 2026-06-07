import random
import time

# Importando  módulos
from Quick_sort import quick_sort
from Bubble_sort import bubble_sort
from Selection_sort import selection_sort
from Insertion_sort import insertion_sort
from Merge_sort import merge_sort
from Heap_sort import heap_sort
from Radix_sort import radix_sort
from Counting_sort import counting_sort
from Bucket_sort import bucket_sort

print("Gerando uma lista de 100.000 números aleatórios para teste...")
dados_teste = [random.randint(1, 100000) for _ in range(100000)]
dados_teste_2 = [random.randint(1, 5000) for _ in range(5000)]
print("Lista Original (primeiros 50):", dados_teste[:50])
print("-" * 50)

# ==========================================
# Algoritmos de Ordenação Rápidos
# ==========================================

# Quick Sort
print("\n[1/6] Executando Quick Sort...")
tempo_incial = time.time()  
lista_ordenada_quick = quick_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_quick[:50])
print(f"Tempo de execução do Quick Sort: {tempo_decorrido:.6f} segundos")

# Merge Sort
print("\n[2/6] Executando Merge Sort...")
tempo_incial = time.time()  
lista_ordenada_merge = merge_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_merge[:50])
print(f"Tempo de execução do Merge Sort: {tempo_decorrido:.6f} segundos")

# Heap Sort
print("\n[3/6] Executando Heap Sort...")
tempo_incial = time.time()  
lista_ordenada_heap = heap_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_heap[:50])
print(f"Tempo de execução do Heap Sort: {tempo_decorrido:.6f} segundos")

# Radix Sort
print("\n[4/6] Executando Radix Sort...")
tempo_incial = time.time()  
lista_ordenada_radix = radix_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_radix[:50])
print(f"Tempo de execução do Radix Sort: {tempo_decorrido:.6f} segundos")

# Counting Sort
print("\n[5/6] Executando Counting Sort...")
tempo_incial = time.time()  
lista_ordenada_counting = counting_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_counting[:50])
print(f"Tempo de execução do Counting Sort: {tempo_decorrido:.6f} segundos")

# Bucket Sort
print("\n[6/6] Executando Bucket Sort...")
tempo_incial = time.time()  
lista_ordenada_bucket = bucket_sort(dados_teste)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_bucket[:50])
print(f"Tempo de execução do Bucket Sort: {tempo_decorrido:.6f} segundos")

print("\n" + "=" * 50)
print("Testes dos algoritmos rápidos concluídos!")
print("=" * 50)

# ==========================================
#           Algoritmos Lentos 
# ==========================================
# Para testar os algoritmos abaixo, o foi preciso reduzir o número de elementos
# da lista de teste por conta do alto tempo de execução em testes anteriores.



# Bubble Sort
print("\nExecutando Bubble Sort...")
tempo_incial = time.time()  
lista_ordenada_bubble = bubble_sort(dados_teste_2)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_bubble[:50])
print(f"Tempo de execução do Bubble Sort: {tempo_decorrido:.6f} segundos")

# Selection Sort
print("\nExecutando Selection Sort...")
tempo_incial = time.time()  
lista_ordenada_selection = selection_sort(dados_teste_2)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_selection[:50])
print(f"Tempo de execução do Selection Sort: {tempo_decorrido:.6f} segundos")

# Insertion Sort
print("\nExecutando Insertion Sort...")
tempo_incial = time.time()  
lista_ordenada_insertion = insertion_sort(dados_teste_2)
tempo_final = time.time()
tempo_decorrido = tempo_final - tempo_incial
print(lista_ordenada_insertion[:50])
print(f"Tempo de execução do Insertion Sort: {tempo_decorrido:.6f} segundos")
