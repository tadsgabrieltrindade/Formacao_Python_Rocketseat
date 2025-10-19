#CLASSE
class Pessoa: 
    # O método especial __init__ é o construtor em Python.
    # Fazendo uma analogia com C#: o construtor de uma classe Pessoa em C# é "public Pessoa() { }". 
    # Em Python usamos __init__(self) para inicializar a instância quando um objeto é criado.
    def __init__(self, nome, idade) -> None: 
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        return f"\nOlá, meu nome é {self.nome}, minha idade é {self.idade}\n"
    

#OBJETOS
pessoa1 = Pessoa("Mike", "42")
print(pessoa1.saudacao())

pessoa2 = Pessoa("Pedro", "21")
print(pessoa2.saudacao())