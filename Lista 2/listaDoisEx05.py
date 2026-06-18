
'''
Ex. 5. 
Você foi contratado para desenvolver um pequeno sistema de
gerenciamento de uma lista de tarefas pessoais. Escreva um
programa em Python que utilize um menu interativo para
permitir ao usuário as seguintes opções:
1. Adicionar uma nova tarefa
2. Listar todas as tarefas
3. Remover uma tarefa pelo nome
4. Sair do programa
O programa deve manter as tarefas em uma lista e permitir
que o usuário realize várias operações até optar por sair.
Utilizar função.
'''
def adicionar(lista):
    lista.append(input("Insira o nome da nova tarefa.\n> ").capitalize())
    return lista

def listar(lista):
    for i in range(len(lista)):
        print(f"Tarefa {i+1}: \"{lista[i]}\"")
    return

def remover(lista):
    while True:
            
        tarefa = input("Insira o nome da tarefa").capitalize()
        if tarefa in lista:
            lista.remove(tarefa)
            print(f"Tarefa \"{tarefa}\" removida.")
            break
        else:
            if int(input("Tarefa não encontrada, deseja tentar novamente?\nDigite 1 para confirmar.\n> ")) == 1:
                pass
            else:
                break

            
        
    return lista
            

def ex5():
    import time
    lista = []
    while True:
        i = int(input('''
=============== Gerenciador de Tarefas ===============
Escolha uma opção.

1 - Adicionar uma nova tarefa
2 - Listar todas as tarefas
3 - Remover uma tarefa pelo nome
4 - Sair

> '''))
        
        if i == 1:
            print("1")
            lista = adicionar(lista)
        elif i == 2:
            listar(lista)
        elif i == 3:
            lista = remover(lista)
        elif i == 4:
            print("Saindo...")
            break
        
            
        #except KeyboardInterrupt:
        #    break
        #except:
        #    print("Algo deu errado, tente novamente.")
        time.sleep(1)
            

if __name__ == "__main__":
    ex5()