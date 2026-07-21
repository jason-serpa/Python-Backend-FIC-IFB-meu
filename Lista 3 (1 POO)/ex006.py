'''6. Desenvolva uma classe Departamento com nome e um vetor
de objetos Funcionario, onde cada funcionário tem nome e
salário, permitindo que funcionários existam
independentemente do departamento para que possam ser
adicionados ou removidos livremente (agregação).
Implemente métodos no Departamento para adicionar
funcionários, calcular a média salarial e listar todos os
funcionários. Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa'''


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, func : Funcionario):
        self.funcionarios.append(func)
        print("Funcionário adicionado com sucesso.")

    def remover_funcionario(self, func : Funcionario):
        self.funcionarios.remove(func)
        print("Funcionário removido com sucesso.")
    
    def calcular_media_sal(self):
        soma = 0
        quant = 0
        for funcionario in self.funcionarios:
            funcionario : Funcionario
            soma+=funcionario.salario
            quant+=1
        print(f"> A média salarial do departamento {self.nome} é de R${soma/quant}")
        return soma/quant
    
    def listar_func(self):
        print(f"> {self.nome}:")
        if self.funcionarios == []:
            print(">> Não há funcionários")
        for func in self.funcionarios:
            print(f">> {func.nome} / {func.salario}")
        return self.funcionarios
        

class Funcionario:
    def __init__(self, nome, salario : float):
        self.nome = nome
        self.salario = salario

'''
 Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa
'''

deps = dict()
funcs = []
deps["Alecrins"] = Departamento(nome="Alecrins")
funcs.append(Funcionario(nome="Alecrim", salario=10))
while True:
    i = int(input('''
===============Gerenciador de Departamento===============
1. Criar departamento
2. Criar funcionário
3. Adicionar funcionário a departamento
4. Listar funcionários
5. Média salarial do sistema
6. Sair
> '''))
    if i == 1:
        '''Criar departamento'''
        nome = input("Insira o nome do departamento:\n> ")
        if nome not in deps:
            deps[nome] = Departamento(nome=nome)
            print(f"Departamento \"{nome}\" criado com sucesso!")
        else:
            print("Departamento já está presente na lista de departamentos.")
    if i == 2:
        '''Criar funcionário'''
        try:
            nome = input("Insira o nome do funcionário:\n> ")
            salario = float(input("Insira o salário do funcionário:\n> "))
            funcs.append(Funcionario(nome=nome, salario=salario))
            print("Funcionário adicionado com sucesso.")
        except Exception as erro:
            print(f"Tente novamente.\n>> ERRO: {erro}")
    if i == 3:
        '''Adicionar funcionário a departamento'''
        try:
            print("Escolha um funcionário para designar a um departamento.")
            quant = 0
            for func in funcs:
                print(f"{quant+1} - {func.nome}")
                quant+=1
            i = int(input("> "))
            if i not in range(quant+1):
                print("Escolha inválida, número não pertencente às escolhas.")
                raise Exception()
            funcionario = funcs[i-1]

            print("\nEscolha um departamento para designar o funcionário.")
            quant = 0
            nomes=[]
            for dep in deps:
                print(f"{quant+1} - {deps[dep].nome}")
                nomes.append(deps[dep].nome)
                quant+=1
            j = int(input("> "))
            if j not in range(quant+1):
                print("Escolha inválida, número não pertencente às escolhas.")
                raise Exception()
            
            
           
            departamento = deps[nomes[quant-1]]
            if funcionario in departamento.funcionarios:
                print("Funcionário já está presente no departamento.")
                raise Exception
            departamento.adicionar_funcionario(func=funcionario)
            print("Funcionário adicionado com sucesso!")
            print(f"> Departamento: {departamento.nome}\n> Funcionário: {funcionario.nome}")
            
        except Exception as err:
            print(f"Tente novamente.\n>>ERRO: {err}")
    if i == 4:
        '''Listar funcionários'''
        print("Funcionários por departamento:")
        for departamento in deps:
            dep : Departamento
            dep = deps[departamento]
            dep.listar_func()
    if i == 5:
        '''Média salarial do sistema'''
        for departamento in deps:
            dep : Departamento
            dep = deps[departamento]
            dep.calcular_media_sal()
    if i == 6:
        break
    