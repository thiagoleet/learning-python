# Projeto Módulo 02 - Jogo
from heroi import Heroi
from inimigo import Inimigo


class Jogo:
    """ Classe orquestradora do jogo """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5,
                           habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos """
        print("\nIniciando a batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagems:")
            print(self.heroi.exibir_detalhes())
            print("\n")
            print(self.inimigo.exibir_detalhes())

            input("\nPressione Enter para atacar...")
            escolha = input(
                "Escolha (1) Ataque Normal - (2) Ataque Especial:")


# Criar instância do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()
