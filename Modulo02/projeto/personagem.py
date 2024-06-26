import random


class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self) -> str:
        return self.__nome

    def get_vida(self) -> int:
        return self.__vida

    def get_nivel(self) -> int:
        return self.__nivel

    def exibir_detalhes(self) -> str:
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def atacar(self, alvo) -> None:
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(
            f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

    def receber_dano(self, dano) -> None:
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
