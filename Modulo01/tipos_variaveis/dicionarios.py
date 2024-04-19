# Dicionários

# Dicionários são coleções não ordenadas de dados que possuem uma chave e um valor associado a ela.

pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print("Pessoa:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
# print("Sobrenome:", pessoa["sobrenome"]) # KeyError

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

# Atualizando valor de um dicionário
pessoa["idade"] = 26
print("Idade:", pessoa["idade"])

# Removendo item do dicionário
del pessoa["cidade"]
print("Pessoa:", pessoa)

# Método keys()
chaves = pessoa.keys()
print("Chaves:", chaves)
print("Chave:", pessoa[list(chaves)[0]])

# Método values()
valores = pessoa.values()
print("Valores:", valores)

# Método items()
itens = list(pessoa.items())
print("Itens:", itens)
