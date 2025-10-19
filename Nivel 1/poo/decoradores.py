# Conceito: Decoradores são funções que recebem outra função (ou callable) e retornam
# uma nova função que envolve a original, permitindo executar código antes e depois,
# modificar entradas/saídas ou alterar comportamento. Em Python aplicamos com @nome_decorador.
# Analogia com middleware (.NET): parecido no sentido de "envolver" comportamento transversal
# (ex.: logging, autenticação), mas decoradores agem em funções/objetos enquanto middleware
# normalmente faz parte do pipeline de requisições/HTTP e recebe um next/nextDelegate.

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()
print("\n")



class MeuDecoradordDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Antes da função ser chamada (decorador da classe)")
        self.func()
        print("Depois da função ser chamada (decorador da classe)")


@MeuDecoradordDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao
