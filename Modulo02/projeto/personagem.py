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
