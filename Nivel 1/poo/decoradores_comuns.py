# @classmethod
# @staticmethod

class MinhaClasse():
    
    __valor = 10 #atributo da classe

    def __init__(self, nome):
        self.nome = nome #atributos da instância 

    #esse método requer a instância para ser chamado 
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome} e o valor é {self.__valor}"
    

    #esse método não consegue acessar os atributos da instância, somente os atributos da classe
    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamada para o valor {cls.__valor}"
    
    #esse metodo não tem acesso a nenhum atributo e não recebe nenhum parâmetros... nem o da instância nem o da classe 
    @staticmethod
    def metodo_estatico():
        return f"Método estático chamado"



obj = MinhaClasse("Philip")
print(obj.metodo_instancia())

print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

#O método de instância/estático é como se fosse o static dentro de uma classe estática no c#, eu chamo sem precisar instanciar um objeto


print("\n")

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    

configuracao1 = "Toyota,Corolla,2025"
carro = Carro.criar_carro(configuracao1)
print(f"Marca: {carro.marca}")
print(f"Modelo: {carro.modelo}")
print(f"Ano: {carro.ano}")

#talvez o ganho de usar o classmethod seja para setar alguns valores globais ou padrões para cada objeto

print("\n   ")

class Matematica:
    
    @staticmethod
    def somar(a, b):
        return a+b
    
print(f"{Matematica.somar(1,2)}")