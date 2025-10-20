#Personagem: classe mãe
#Heroi e Inimigo: Herdam de personagem
#Hero é controlado pelo usuario e inimigo pelo pc

import random

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
    
    def ataque(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou o {alvo.get_nome()} e causou {dano} de dano")

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou o {alvo.get_nome()} e causou {dano} de dano com a habilidade especial {self.get_habilidade()}")



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
    def __init__(self):
        self.heroi = heroi = Heroi("Heroi", 100, 5, "Super Força")
        self.inimigo = inimigo = Inimigo("Morcego", 50, 3, "Voador")    
    
    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("\nBatalha iniciada")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("\nPresione enter para atacar")
            escolha = input("Ataque normal(1) ou o ataque especial(2)?\nEscolha: ")

            if escolha == "1":
                self.heroi.ataque(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida, tente novamente!")

            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque(self.heroi)

        if self.heroi.get_vida() > 0: 
            print("Parabéns, você venceu!")
        else:
            print("Você foi derrotado!")





jogo = Jogo()
jogo.iniciar_batalha()