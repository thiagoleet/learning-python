# Listas

# Declaração

minha_lista = [1,2,3,4,5, "John", True]
minha_lista = ["Java", "C#", "Python", "Ruby", "JavaScript", "C++", "Rust"]

print("Minha Lista:", minha_lista)

print("Tamanho da Lista:", len(minha_lista))

print("Elemento índice 0:", minha_lista[0])

minha_lista[0] = "Python"

print("Elemento índice 0:", minha_lista[0])

print("Elemento índice 5:", minha_lista[5])

print("Intervalo (Fatia):", minha_lista[1:3])
print("Intervalo (Fatia):", minha_lista[2:])
print("Intervalo (Fatia):", minha_lista[:4])

# Métodos de Lista

# Método append()
minha_lista.append("Java")
print("Apóis append()", minha_lista)

# Método index()
# print("Index de 5:", minha_lista.index(5))

# Método insert()
minha_lista.insert(2, "C++")
print("Após insert()", minha_lista)

# Método pop()
elemento_devido = minha_lista.pop(2)
print("Após pop()", minha_lista)

# Método remove()
minha_lista.remove("Java")
print("Após remove()", minha_lista)

# Método sort()
minha_lista.sort()
print("Após sort()", minha_lista)