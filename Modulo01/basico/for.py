# Estruturas de Laço (FOR)

# for utilizando lista
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

# for utilizando tupla
tupla = ("A", "B", "C", "D", "E")

for elemento in tupla:
    print(elemento)

# for utilizando dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

# for utilizando dicionário -- chaves
for chave in pessoa.keys():
    print(chave)

# for utilizando dicionário -- valores
for valor in pessoa.values():
    print(valor)

# for utilizando dicionário -- chave + valor
for chave in pessoa.keys():
    print(f"{chave}: {pessoa[chave]}")


# for utilizando dicionario -- itens
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# for utilizando range()
for numero in range(1, 6):
    print(f"Número: {numero}")

for indice in range(0, len(lista)):
    print(f"Índice: {indice} - Elemento: {lista[indice]}")

# enumerate
lista_enumerate = ["a", "b", "c", "d"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Este é o índice 1")
