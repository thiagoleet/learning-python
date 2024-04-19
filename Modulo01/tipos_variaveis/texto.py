# tipos de texto

# Declaração
nome_completo = "John Doe"
print("Nome completo = ", nome_completo, type(nome_completo))

nome_completo_aspas = """John
Doe"""
print("Nome completo aspas triplas = ", nome_completo_aspas, type(nome_completo_aspas))

nome_completo_quebra = "John\nDoe"
print("Nome completo quebra", nome_completo_quebra, type(nome_completo_quebra))


nome = "John"
sobrenome = "Doe"

# Formatação
print("Nome Completo (1a forma):", nome_completo)
print("Nome Completo (2a forma):" + nome_completo)
print("Nome Completo (3a forma): " + nome + " " + sobrenome)
print("Nome Completo (4a forma): " + nome, sobrenome)
print("Nome Completo (5a forma):", nome_completo_aspas)
print("Nome Completo (6a forma):", nome_completo_quebra)
print("Nome Completo (7a forma): %s" % nome_completo)
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome Completo (9a forma):  {nome}  {sobrenome}")
print("Nome Completo (10a forma):  {}  {}".format(nome, sobrenome))

