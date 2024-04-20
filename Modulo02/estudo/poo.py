# Programação Orientada à Objetos

# Classe
class Pessoa:
    # -> None indica que não tem retorno, é um método construtor
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        pass

    def saudacao(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


# Criando um objeto
pessoa1 = Pessoa("Alice", 30)

# print(f"Nome: {pessoa1.nome}")
# print(f"Idade: {pessoa1.idade}")
print(pessoa1.saudacao())

pessoa2 = Pessoa("Rodrigo", 32)
print(pessoa2.saudacao())
