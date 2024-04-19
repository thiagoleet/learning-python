# Principais métodos de texto
nome = "John"
sobrenome = "Doe"
nome_completo = "John Doe"

print(nome.upper(), sobrenome.lower())
print(nome[0], nome[1], nome[2], nome[3])


print(nome_completo.count("o"))
find = nome_completo.find("o")
print(nome_completo[find])

print(nome.encode(), nome.encode().decode())
print(nome_completo.replace("o", "0"))

telefone = "(11) 99999-9999"

print(telefone, telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

print("-".join(nome))

print(nome_completo.split(" "))

nome_sujo = "xJohn Doex"
print(nome_sujo.strip("x"))

print(nome_completo.startswith("J"))
print(nome_completo.endswith("J"))

print("Silva" in nome_completo)
print("Silva" not in nome_completo)