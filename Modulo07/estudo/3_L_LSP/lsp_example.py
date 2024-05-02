# SOLID - Liskov Substitution Principle (LSP)

class Animal:
    def comer(self) -> None:
        print("O animal está comendo")

    def andar(self) -> None:
        print("O animal está andando na jaula")


class Felino(Animal):
    def lamber(self) -> None:
        print("O felino está lambendo seu pelo")


class Leao(Felino):
    def rugir(self) -> None:
        print("O leão está rugindo alto!!!")


class Pessoa:
    def observa(self, animal: Animal) -> None:
        print("A pessoa está observando o animal")
        animal.comer()


animal = Animal()
felino = Felino()
leao = Leao()
renatinho = Pessoa()

renatinho.observa(animal)
renatinho.observa(felino)
renatinho.observa(leao)

# animal.comer()
# felino.comer()
# leao.comer()
