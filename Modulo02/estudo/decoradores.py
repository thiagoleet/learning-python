# Decoradores

def meu_decorador(func):
    # Wrapper
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()


class MeuDecoradorClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")


@MeuDecoradorClasse
def minha_segunda_funcao():
    print("Segunda função foi chamada")


minha_segunda_funcao()
