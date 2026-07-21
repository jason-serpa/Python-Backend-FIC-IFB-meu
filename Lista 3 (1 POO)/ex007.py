
'''7. Implemente uma classe Casa que contenha vários objetos do
tipo Comodo, sendo que cada cômodo possui nome (ex: sala,
cozinha, banheiro) e área. Os cômodos devem ser
implementados de forma que só existam se a casa existir
(relação de composição), e não devem ser acessados ou
manipulados diretamente de fora. Implemente um método na
casa para calcular a área total, somando as áreas de todos os
cômodos. Desenvolva um programa com menu interativo no
console que permita criar uma casa, adicionar cômodos à
casa, listar os cômodos da casa, calcular e exibir a área total
da casa e encerrar o programa.'''

class Comodo:
    def __init__(self, nome, area : float):
        self.__nome = nome
        self.__area = area
    def get_nome(self):
        return self.__nome
    def get_area(self):
        return self.__area
    def set_nome(self, newNome):
        self.__nome = newNome
    def set_area(self, newArea):
        self.__area = newArea

class Casa:
    def __init__(self, nome):
        self.nome = nome
        self.__comodos = []

    def adicionar_area(self):
        nome = input("Informe o nome do cômodo:\n> ")
        area = float(input("Informe a área do cômodo, em metros:\n> "))
        self.__comodos.append(Comodo(nome=nome, area=area))

    def calcular_area(self):
        soma = 0
        for comodo in self.__comodos:
            soma += comodo.get_area()
        print("\nA área total da casa é ", soma, "m", sep="")
    
    def get_comodos(self):
        return self.__comodos
    def set_comodos(self, newCom):
        self.__comodos = newCom

casas = []
while True:
    i = int(input('''
=============Gerenciador de Casas=============
1. Criar um casa
2. Adicionar cômodos
3. Listar cômodos
4. Calcular área total              
5. Encerrar programa              
> '''))
    if i == 1:
        casas.append(Casa(nome=input("Insira o nome da casa:\n> ")))
        print("Casa criada com sucesso")
    if i == 2:
        try:
            print("Escolha o número da casa:")
            quant = 0
            for casa in casas:
                quant+=1
                print(f"{quant} - {casa.nome}")
            i = int(input("> "))
            if i not in range(quant+1):
                print("Escolha inválida.")
                raise Exception
            casas[i-1].adicionar_area()
        except Exception as err:
            print(f"Algo deu errado.\n>>ERRO: {err}")
    if i == 3:
        try:
            print("Escolha o número da casa:")
            quant = 0
            for casa in casas:
                quant+=1
                print(f"{quant} - {casa.nome}")
            i = int(input("> "))
            if i not in range(quant+1):
                print("Escolha inválida.")
                raise Exception
            casa = casas[i-1]
            casa : Casa
            print("-"*20)
            print(f"> Casa {casa.nome}")
            for comodo in casa.get_comodos():
                comodo : Comodo
                nome = comodo.get_nome()
                area = comodo.get_area()
                print(f">> {nome}: {area}m")

        except Exception as err:
            print(f"Algo deu errado.\n>>ERRO: {err}")
    if i == 4:
        try:
            print("Escolha o número da casa:")
            quant = 0
            for casa in casas:
                quant+=1
                print(f"{quant} - {casa.nome}")
            i = int(input("> "))
            if i not in range(quant+1):
                print("Escolha inválida.")
                raise Exception
            casas[i-1].calcular_area()
        except Exception as err:
            print(f"Algo deu errado.\n>>ERRO: {err}")
    if i == 5:
        break
    
