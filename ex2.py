'''
1. Permitir que o usuário adicione tarefas. Cada tarefa deve ter:
Descrição (string), Prioridade (inteiro de 1 a 5, onde 1 é a prioridade
mais alta) e Status (inicialmente “pendente”);

2. Armazenar cada tarefa como um dicionário com as chaves
"descrição", "prioridade" e "status";

3. Manter todas as tarefas numa lista;

4. Criar funções para: Adicionar tarefas, Mostrar todas as tarefas
ordenadas por prioridade (da maior para a menor) e Marcar uma
tarefa como concluída (alterar o status para “concluída”);

5. Criar uma função main() que permita ao usuário escolher opções
num menu para: Adicionar tarefa, Listar tarefas, Marcar tarefa como
concluída e Sair do programa.
'''


def Adicionar(tarefas):
    desc = input("Insira uma descrição para a tarefa:\n")
    priority = input("Insira a prioridade da tarefa:\n")
    status = input("Insira o status da tarefa:\n")
    if status == "":
        tarefas.append([desc, priority, "Pendente"])
    else:
        tarefas.append([desc, priority, status])
        
    return tarefas

def Listar(tarefas):
    contagem = 1
    for item in tarefas:
        print(f"Tarefa {contagem}: {item}")
        contagem += 1
        
    return

def Marcar(tarefas):
    print("Selecione uma tarefa da lista pelo número:\n")
    contagem = 1
    for item in tarefas:
        print(f"Tarefa {contagem}: {item}")
        contagem += 1
    select = int(input("\n\nQual sua escolha?\n"))

    tarefas[select-1][2] = "Concluído"
    
    return tarefas


def main():
    tarefas = []
    loop = 1
    escolha = int(input(
'''
=====================================
Escolha uma opção:
1. Adicionar tarefas
2. Listar tarefas
3. Marcar tarefa como concluída
4. Sair do programa
=====================================
'''))
    while loop:
        if escolha == 1:
            tarefas = Adicionar(tarefas)
        elif escolha == 2:
            Listar(tarefas)
        elif escolha == 3:
            tarefas = Marcar(tarefas)
        elif escolha == 4:
            Sair()
        else:
            print("Escolha inválida, reiniciando programa...")
            return main()
        escolha = int(input(
        '''
=====================================
Escolha uma opção:
1. Adicionar tarefas
2. Listar tarefas
3. Marcar tarefa como concluída
4. Sair do programa
=====================================
'''))
        if escolha == 4:
            raise Exception
        

if __name__ == "__main__":
    main()
