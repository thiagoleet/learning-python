# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10  # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome  # Atributo de instância

    # requer uma instância para ser chamado
    def metodo_instancia(self) -> str:
        return f"Metodo de instância chamado, {self.nome}"

    # Método da classe
    @classmethod
    def metodo_classe(cls) -> str:
        return f"Método de classe chamado, {cls.valor}"

    # Método estático
    @staticmethod
    def metodo_estatico() -> str:
        return "Método estático chamado"


obj = MinhaClasse(nome="Classe Exemplo")
print(obj.nome)
print(obj.metodo_instancia())
# print(MinhaClasse.metodo_instancia()) # Não funciona
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))


configuracao1 = "Ford,Fiesta,2013"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")


class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b


print(Matematica.somar(10, 20))
