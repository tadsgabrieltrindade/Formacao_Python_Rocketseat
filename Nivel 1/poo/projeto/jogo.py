#Personagem: classe mãe
#Heroi e Inimigo: Herdam de personagem
#Hero é controlado pelo usuario e inimigo pelo pc

class Personagem: 
    def __init__(self, nome, vida, nivel ):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"



class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
    


class Jogo:
    """Classe orquestradora do jogo"""
    self.heroi = heroi = Heroi("Heroi", 100, 5, "Super Força")
    self.inimigo = inimigo = Inimigo("Morcego", 50, 3, "Voador")
    
    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("\nBatalha iniciada")
        # while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
        #     print("\n")