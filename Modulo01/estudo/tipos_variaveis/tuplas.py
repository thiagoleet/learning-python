# Tuplas
# Uma coleção ordenada e imutável de elementos

minha_tupla = (1, 2, 3, 4, 5)
print("Minha tupla:", minha_tupla)

print("Primeiro Elemento:",  minha_tupla[0])
print("Elemento Índice 2:", minha_tupla[2])
print("Primeiro índice negativo:", minha_tupla[-1])

# Método count()
contagem = minha_tupla.count(2)
print("Quantidade de 2 na tupla:", contagem)

indice = minha_tupla.index(3)
print("Índice do elemento 3:", indice)
