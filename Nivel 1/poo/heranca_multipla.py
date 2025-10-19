class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som():
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"O animal mamifério {self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"O animal ave {self.nome} está voando"

#HERANÇA MULTIPLA - Herda de duas classes
class Morcego(Mamifero, Ave): 
    def emitir_som(self):
        return f"O animal morcego {self.nome} está emitindo som"
    

morcego = Morcego("Batman")
print(f"\n{morcego.amamentar()}")
print(f"\n{morcego.voar()}")
print(f"\n{morcego.emitir_som()}")