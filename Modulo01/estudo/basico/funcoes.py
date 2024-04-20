# Funções

def saudacao(nome):
    print(f"Olá, {nome}")


print("\nChamndo a função saudacao()")
saudacao("Alice")
saudacao("Bob")


# funcão com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado


print("\nChamando a função quadrado()")
print(quadrado(2))
print(quadrado(5))


# função com múltiplos parâmetros

def soma(a, b):
    return a + b


print("\nChamando a função soma()")
print(soma(2, 3))
numero1 = 10
numero2 = 15
print(soma(numero1, numero2))
