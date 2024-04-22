# Projeto Módulo 02 - Jogo
from heroi import Heroi
from inimigo import Inimigo

heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
print(heroi.exibir_detalhes())

inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")
print(inimigo.exibir_detalhes())
