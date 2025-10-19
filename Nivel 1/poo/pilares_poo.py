#Pilares do POO
#HERANÇA, POLIMORFISMO, ENCAPSULAMENTO E ABSTRAÇÃO

#HERANÇA E POLIMORFISMO
class Animal: 
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

    def andar(self, msg=None):
        if msg is None:
            msg = f"O animal {self.nome} andou"
        return msg
    
    def to_string(self):
        return f"\nNome: {self.nome} \nSom: {self.emitir_som()} \nAndou? {self.andar()}\n"


class Cachorro(Animal):
    #Polimorfismo
    def emitir_som(self):
        return "Au, au"
    
    def andar(self):
        return super().andar(f"O animal {self.nome} não andou")
    


class Gato(Animal):
    #Polimorfismo
    def emitir_som(self):
        return "Miau!"
    

# animal = Animal("Dougue")
# print(animal.to_string())

# cachorro = Cachorro("Mk")
# print(cachorro.to_string())

# gato = Gato("Mk")
# print(gato.to_string())


#ENCAPSULAMENTO 
class ContaBancaria():
    def __init__(self, saldo):
        self.__saldo = saldo #o __ significa private 


    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado! Seu saldo é de R${self.__saldo}")
    
    def sacar(self, valor):
        if self.__saldo >= valor and valor > 0:
            self.__saldo -= valor
            print(f"Saque realizado! Seu saldo é de R${self.__saldo}")
        else:
            print(f"Saldo insulficiente. Seu saldo é de R${self.__saldo}")

    
    def get_saldo(self):
        return self.__saldo
    




# conta = ContaBancaria(2394)
# print(f"\nSaldo atual R${conta.get_saldo()}")
# conta.depositar(100)
# conta.sacar(2494)



#ABSTRAÇÃO
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca):
        self.marca = marca
    
    def ligar(self):
        return super().ligar()
    
    def desligar(self):
        return super().desligar()



carro = Carro("Fiat")
print(f"{carro.marca}")



print("\n")