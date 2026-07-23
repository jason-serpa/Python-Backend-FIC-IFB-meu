'''
10. Implemente um sistema em Python para representar
personagens do universo dos Cavaleiros do Zodíaco,
utilizando herança múltipla. Crie uma classe Personagem
com os atributos nome e constelacao, e métodos como
apresentar(). Crie também duas classes auxiliares:
CavaleiroDeBronze com o atributo poder_de_luta e um
método golpe_especial(), e CavaleiroDeOuro com o atributo
casa_do_zodiaco e um método defender_casa(). Em
seguida, implemente a classe CavaleiroHibrido, que herda
tanto de CavaleiroDeBronze quanto de CavaleiroDeOuro,
combinando os comportamentos de ambas. O programa deve
oferecer um menu interativo no console com as opções de
cadastrar personagens, listar todos os personagens, executar
os golpes especiais ou defesas, e encerrar o programa.
Explore o uso da herança múltipla e do polimorfismo para
definir o comportamento de cada tipo de cavaleiro'''

class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao
    
    def apresentar(self):
        return f"Sou {self.nome}, cavaleiro de {self.constelacao}!"
        

class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poderDeLuta):
        Personagem.__init__(self, nome=nome, constelacao=constelacao)
        self.poderDeLuta = poderDeLuta
    def golpe_especial(self):
        print("\nMeteoro de ", self.constelacao, "!", sep="")

class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casaZodiaco):
        Personagem.__init__(self, nome=nome, constelacao=constelacao)
        self.casaZodiaco = casaZodiaco
    def defender_casa(self):
        print("\nO cavaleiro de ", self.casaZodiaco, " defende sua casa!", sep="")

class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poderDeLuta, casaZodiaco):
        CavaleiroDeBronze.__init__(self, nome=nome, constelacao=constelacao, poderDeLuta=poderDeLuta)
        CavaleiroDeOuro.__init__(self, nome=nome, constelacao=constelacao, casaZodiaco=casaZodiaco)
    

'''O programa deve
oferecer um menu interativo no console com as opções de
cadastrar personagens, listar todos os personagens, executar
os golpes especiais ou defesas, e encerrar o programa.
Explore o uso da herança múltipla e do polimorfismo para
definir o comportamento de cada tipo de cavaleiro
'''

cavaleiros = []
cavaleiros.append(CavaleiroDeBronze(nome="Seiya", constelacao="Pégaso", poderDeLuta=1000))
cavaleiros.append(CavaleiroDeOuro(nome="Camus", casaZodiaco="Aquário", constelacao="Aquário"))
while True:
    i = int(input('''
================Saint Seiya================
1. Cadastrar personagens
2. Listar personagens
3. Executar golpes especiais ou defesas
4. Sair do programa
> '''))
    if i == 1:
        '''1. Cadastrar personagens'''
        nome = input("Insira o nome do personagem:\n> ").capitalize()
        escolha = int(input("O personagem é um cavaleiro de bronze ou de ouro?\n1- Bronze\n2- Ouro\n3- Ambos\n> "))
        cons = input("Qual a constelação do personagem?\n> ")
        if escolha == 1:
            poder = float(input("Insira o poder de luta do personagem:\n> "))
            cavaleiros.append(CavaleiroDeBronze(nome=nome, constelacao=cons, poderDeLuta=poder))
        elif escolha == 2:
            zod = input("Qual a casa do zodíaco do personagem?\n> ")
            cavaleiros.append(CavaleiroDeOuro(nome=nome, constelacao=cons, casaZodiaco=zod))
        elif escolha == 3:
            poder = float(input("Insira o poder de luta do personagem:\n> "))
            zod = input("Qual a casa do zodíaco do personagem?\n> ")
            cavaleiros.append(CavaleiroHibrido(nome=nome, constelacao=cons, casaZodiaco=zod, poderDeLuta=poder))
        else:
            print("Escolha inválida")
        
    if i == 2:
        '''2. Listar personagens'''
        print("Cavaleiros:")
        for cav in cavaleiros:
            print(">", cav.nome)
            print(">> Cavaleiro de", cav.constelacao)
            if type(cav) == CavaleiroDeBronze:
                print(">> Cavaleiro de Bronze")
                print(">> Poder de luta:", cav.poderDeLuta)
            elif type(cav) == CavaleiroDeOuro:
                print(">> Cavaleiro de Ouro")
                print(">> Casa de", cav.casaZodiaco)
            elif type(cav) == CavaleiroHibrido:
                print(">> Cavaleiro Híbrido")
                print(">> Poder de luta:", cav.poderDeLuta)
                print(">> Casa de", cav.casaZodiaco)
            print(">>> Apresentação:", cav.apresentar(), "\n")

    if i == 3:
        '''3. Executar golpes especiais ou defesas'''
        print("Escolha um cavaleiro:")
        quant = 0
        for cav in cavaleiros:
            quant+=1
            print(quant, "-", cav.nome)
        i = int(input("> "))
        cav = cavaleiros[i-1]
        if type(cav) == CavaleiroDeBronze or type(cav) == CavaleiroHibrido:
            cav.golpe_especial()
        if type(cav) == CavaleiroDeOuro or type(cav) == CavaleiroHibrido:
            cav.defender_casa()

        
    if i == 4:
        break
    