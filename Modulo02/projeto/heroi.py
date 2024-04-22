from personagem import Personagem


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self) -> str:
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
