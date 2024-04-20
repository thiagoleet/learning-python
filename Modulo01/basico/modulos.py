# Módulos
# import math #importa o módulo todo
# import meu_modulo
from meu_modulo import saudacao, dobro
from math import sqrt  # importa somente o que precisa

print("\nExemplo de importação de módulo padrão")


# raiz_quadrada = math.sqrt(25)
raiz_quadrada = sqrt(25)
print(f"\nA raíz quadrada é {raiz_quadrada}")


print("\nExemplo de criação de um módulo personalizado")


# mensagem = meu_modulo.saudacao("John")
# resultado_dobro = meu_modulo.dobro(5)
mensagem = saudacao("John")
resultado_dobro = dobro(5)

print(mensagem)
print(resultado_dobro)
