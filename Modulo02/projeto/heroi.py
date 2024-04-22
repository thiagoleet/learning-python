from personagem import Personagem
import random


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self) -> str:
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo) -> None:
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_dano(dano)
        print(
            f"\n{self.get_nome()} usou sua habilidade especial {self.get_habilidade()} e causou {dano} de dano")
