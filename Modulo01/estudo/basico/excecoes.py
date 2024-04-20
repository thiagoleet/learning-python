# Exceções
print("Exemplo de captura de exceções")

try:
    numero = int(input("\nDigite um número inteiro: "))
    resultado = int(10 / numero)
except ValueError as e:
    print(f"\nErro de ValueError: {e}")
    # raise ValueError("Tipo de variáveis incompatíveis")
except Exception as e:
    print(f"\nErro: {e}")
else:
    print(f"\nO resultdo é {resultado}")
finally:
    print("\nOperação finalizada")
