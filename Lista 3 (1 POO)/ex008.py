
'''8. Desenvolva um sistema em Python para representar
personagens de um jogo de RPG. Crie uma classe base
chamada Personagem, com os atributos nome e nivel, e um
método atacar() que imprime uma mensagem genérica de
ataque. Em seguida, crie as subclasses Guerreiro e Mago. A
classe Guerreiro deve possuir o atributo adicional forca e
sobrescrever o método atacar() para exibir uma mensagem de
ataque físico, enquanto a classe Mago deve ter o atributo
mana e sobrescrever o método atacar() para representar um
ataque mágico. Na classe principal, crie instâncias das três
classes e invoque o método atacar() para demonstrar o uso
de herança e polimorfismo em tempo de execução.
'''

class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
    def atacar(self):
        print(f"{self.nome}: Arranhão!")

class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana
    def atacar(self):
        print(f"{self.nome}: Corte rápido!")

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.forca = forca
    def atacar(self):
        print(f"{self.nome}: Bola de fogo!")


rato = Personagem(nome="Rato", nivel=1)
guerreiro = Guerreiro(nome="Espadachim", nivel=10, forca=100)
mago = Mago(nome="Feiticeiro", nivel=10, mana=100)

print(f"\n{rato.nome} ataca!")
rato.atacar()

print(f"\n{guerreiro.nome} ataca!")
guerreiro.atacar()

print(f"\n{mago.nome} ataca!")
mago.atacar()