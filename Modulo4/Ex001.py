'''Objetivo:
Construir um sistema simples de gerenciamento de tarefas no terminal, aplicando:
MVC (Model-View-Controller) para estruturar o sistema;
Singleton para garantir apenas uma instância da classe que simula o banco de dados;
Observer para atualizar automaticamente a interface (View) quando as tarefas forem alteradas.

Enunciado
Você foi contratado para desenvolver um Sistema de Lista de Tarefas no terminal.
O sistema deverá permitir:
Adicionar uma nova tarefa
Listar todas as tarefas
Marcar uma tarefa como concluída
'''

class Tarefa(): #Model
    '''Tarefa individual'''
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False

    
class View(): #View
    def visualizar(self, tarefas):
        print("-"*20,"Lista de Tarefas","-"*20)
        index = 0
        for tarefa in tarefas:
            index+=1
            print(f"- {index}: {tarefa.nome}")
            print(f"- Status: {'Concluído' if tarefa.concluida==True else 'Pendente'}")
        print("")


class BancoDeTarefas(): #Model (Singleton)
    '''Guarda coleção de tarefas e notifica observadores'''
    _instancia = None

    def __new__(cls):
        if cls._instancia == None:
            cls._instancia = object.__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "tarefas"): #Checa se já existe instância, já que singleton necessita ter uma única
            self.tarefas = []
            self.observers = []

    def adicionarTarefa(self, tarefa : Tarefa):
        self.tarefas.append(tarefa)
        self.notificarObservador()

    def marcarTarefa(self, tarefa : Tarefa):
        tarefa.concluida = True
        self.notificarObservador()

    def listarTarefas(self,):
        return self.tarefas 
    
    def adicionarObservador(self, observer : View):
        self.observers.append(observer)

    def notificarObservador(self):
        for observer in self.observers:
            observer.visualizar(self.tarefas)


class Controller(): #Controller
    '''Recebe input e aciona Model e View'''
    def __init__(self): 
        self.banco = BancoDeTarefas()
        self.view = View() 
        self.banco.adicionarObservador(self.view)
    def executar(self):
        while True:
            print("1 - Adicionar tarefa")
            print("2 - Listar tarefas")
            print("3 - Marcar tarefa como concluída")
            print("4 - Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                tarefa = input("Insira o nome da tarefa:\n> ").upper()
                self.banco.adicionarTarefa(Tarefa(tarefa))
            elif opcao == "2":
                self.view.visualizar(tarefas=self.banco.tarefas)
            elif opcao == "3":
                tarefa = input("Insira o nome da tarefa:\n> ").upper()
                placeholder_tarefa = tarefa
                for task in self.banco.tarefas:
                    task : Tarefa
                    if tarefa == task.nome:
                        tarefa = task
                        break
                if tarefa == placeholder_tarefa:
                    print("Tarefa não encontrada.") 
                else:
                    self.banco.marcarTarefa(tarefa=tarefa)
            elif opcao == "4":
                break

if __name__ == "__main__":
    app = Controller()
    app.executar()