# Herança Múltipla

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self) -> str:
        pass


class Mamifero(Animal):
    def amamentar(self) -> str:
        return f"{self.nome} está amamentando"


class Ave(Animal):
    def voar(self) -> str:
        return f"{self.nome} está voando"


class Morcego(Mamifero, Ave):
    def emitir_som(self) -> str:
        super().emitir_som()
        return "Morcego emitem sons ultrasônicos"


morcego = Morcego(nome="Batman")

# Acessando os métodos da classe base Animal
print(f"Nome do morcego: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando os métodos das classes Mamifero e Ave
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")
