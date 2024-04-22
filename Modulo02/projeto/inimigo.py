from personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self) -> str:
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
