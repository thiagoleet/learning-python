# Pilares de Programação Orientada a Objetos

# Herança

print("\nExemplo de Herança")


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self) -> str:
        pass

    def andar(self) -> None:
        print(f"\nO animal {self.nome} andou")
        pass


class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "Au Au"


class Gato(Animal):
    def emitir_som(self) -> str:
        return "Miau"


dog = Cachorro("Rex")
cat = Gato("Felix")

# Polimorfismo
print("\nExemplo de Polimorfismo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz {animal.emitir_som()}")

# Encapsulamento
print("\nExemplo de Encapsulamento")


class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor) -> None:
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor) -> None:
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self) -> float:
        return self.__saldo


conta = ContaBancaria(1000)
print(f"Saldo: {conta.consultar_saldo()}")
conta.depositar(500)
print(f"Saldo: {conta.consultar_saldo()}")
conta.depositar(-100)
print(f"Saldo: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)
