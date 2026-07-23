
'''12. No universo de Dragon Ball, desenvolva um sistema em
Python para simular um torneio de artes marciais, utilizando
orientação a objetos. Crie uma classe totalmente abstrata
chamada Lutador, contendo apenas métodos abstratos para
obter o nome do lutador, o nível de poder e realizar um
ataque. Em seguida, implemente subclasses como Saiyajin,
Androide e Namekuseijin, cada uma com um comportamento
específico ao atacar. O sistema deve conter um menu
interativo que permita cadastrar lutadores de diferentes raças,
listar todos os lutadores inscritos no torneio e simular
ataques, demonstrando o uso de herança, abstração total e
polimorfismo. Implemente também tratamento de exceções,
garantindo que os nomes não estejam vazios e que o nível de
poder seja um valor numérico positivo.'''

from abc import ABC, abstractmethod
class Lutador(ABC):
    @abstractmethod
    def get_nome(self):
        pass
    @abstractmethod
    def get_nivel(self):
        pass
    @abstractmethod
    def atacar(self):
        pass
    
class Saiyajin(Lutador):
    def __init__(self, nome, nivel):
        self.__nome = nome
        self.__nivel = nivel
    def get_nome(self):
        return self.__nome
    def get_nivel(self):
        return self.__nivel
    def atacar(self):
        print("Galick GUN!!")
    
class Androide(Lutador):
    def __init__(self, nome, nivel):
        self.__nome = nome
        self.__nivel = nivel
    def get_nome(self):
        return self.__nome
    def get_nivel(self):
        return self.__nivel
    def atacar(self):
        print("Absorção!!")
    
class Namekuseijin(Lutador):
    def __init__(self, nome, nivel):
        self.__nome = nome
        self.__nivel = nivel
    def get_nome(self):
        return self.__nome
    def get_nivel(self):
        return self.__nivel
    def atacar(self):
        print("Makanko Sappo!!")
    

'''O sistema deve conter um menu
interativo que permita cadastrar lutadores de diferentes raças,
listar todos os lutadores inscritos no torneio e simular
ataques, demonstrando o uso de herança, abstração total e
polimorfismo. Implemente também tratamento de exceções,
garantindo que os nomes não estejam vazios e que o nível de
poder seja um valor numérico positivo.'''


lutadores = []
lutadores.append(Saiyajin(nome="Vegeta", nivel=8000))
lutadores.append(Namekuseijin(nome="Piccolo", nivel=8000))
lutadores.append(Androide(nome="Cell", nivel=2000))

while True:
    i = int(input('''
================DBZ================
1. Cadastrar lutador
2. Listar lutadores no torneio
3. Simular torneio
4. Sair do programa
> '''))
    if i == 1:
        '''1. Cadastrar lutadores'''
        try:
            nome = input("Insira o nome do lutador:\n> ")
            raca = input("Qual a raça do lutador?\n1- Saiyajin\n2- Namekuseijin\n3- Androide\n> ")
            nivel = input("")
            if not nome.isalpha():
                raise ValueError("Nome inválido.")
            elif raca not in list("0", "1" ,"2"):
                raise IndexError("Raça inválida.")
            elif not nivel.isnumeric() or float(nivel) < 0:
                raise ValueError("Poder inválido.")

            if raca == "1": #Saiyajin
                lutadores.append(Saiyajin(nome=nome, nivel=nivel))
            elif raca == "2": #Namek
                lutadores.append(Namekuseijin(nome=nome, nivel=nivel))
            elif raca == "3": #Android
                lutadores.append(Androide(nome=nome, nivel=nivel))
            
        except Exception as err:
            print(">> ERRO:", err)
        
        
    if i == 2:
        '''2. Listar lutadores no torneio'''
        print("Lutadores no torneio:")
        for lutador in lutadores:
            print(">", lutador.get_nome())
            print(">> Poder de luta:", lutador.get_nivel())
            print(">> Raça:", type(lutador).__name__)  
        print()


    if i == 3:
        for lutador in lutadores:
            print(lutador.get_nome(), ":", sep="")
            lutador.atacar()
            print()
        
    if i == 4:
        break
    