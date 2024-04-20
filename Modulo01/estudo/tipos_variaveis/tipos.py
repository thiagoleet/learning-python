# Tipos numéricos

# Números Inteiros
numero_inteiro = 42
print("Inteiro = ", numero_inteiro)

# Números Reais
numero_real = 3.14
print("Real = ", numero_real) 

# Função type()
print("Tipo de dado de numero_inteiro = ", type(numero_inteiro))
print("Tipo de dado de numero_real = ", type(numero_real))

# soma
soma =  1 + 2
print("Soma = ", soma, type(soma))
print("Soma = ", float(soma), type(float(soma)))

# subtração
subtracao = 2 - 1
print("Subtração = ", subtracao)

# multiplicação
multiplicacao = 2 * 3
print("Multiplicação = ", multiplicacao)

# divisão
divisao = 5 / 2
print("Divisão = ", divisao, type(divisao))
print("Divisão (int) = ", int(divisao), type(int(divisao)))

# divisão inteiro
divisao_inteiro = 5 // 2
print("Divisão Inteiro = ", divisao_inteiro, type(divisao_inteiro))

# resto da divisão
resto = 5 % 2
print("Resto = ", resto)

if resto == 0:
    print("O número 5 é par")
else:
  print("O número é ímpar")