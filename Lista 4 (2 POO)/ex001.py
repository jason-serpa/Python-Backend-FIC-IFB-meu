'''1. Implemente um sistema de gerenciamento de cursos e alunos em Python, utilizando
orientação a objetos. O sistema deve funcionar por meio de um menu interativo e permitir as
seguintes operações:
Listar todos os alunos cadastrados.
Listar todos os cursos cadastrados.
Matricular um aluno em um curso.
Exibir em quais cursos um aluno está matriculado.
Encerrar o programa.
Os alunos e cursos já devem estar previamente cadastrados no início do programa. O
usuário poderá escolher as opções pelo menu, realizar matrículas e consultar as
informações desejadas. Cada aluno pode se matricular em vários cursos, e cada curso pode
ter vários alunos.'''

"""
Sistema de Gerenciamento de Cursos e Alunos
Menu interativo com operações de listagem e matrícula.
"""
class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.cursos = []
        
    def matricular(self, curso : Curso):
        i = input(f"Deseja inscrever o(a) aluno(a) \"{self.nome}\" no curso \"{curso.nome}\"?\n1- Sim\n2- Não\n> ")
        if i != "1":
            return
        for cursop in self.cursos:
            if curso.nome == cursop.nome:
                print("Aluno já está matriculado.")
                return
        self.cursos.append(curso)
        curso.adicionar(self)

        
        
class Curso:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.alunos = []
    def adicionar(self, aluno : Aluno):
        if aluno.nome not in self.alunos:
            self.alunos.append(aluno)
            print("Aluno(a) matriculado com sucesso.")
        

def main():
    alunos = [Aluno("001", "José Miguel"), Aluno("002", "Ana Clara"), Aluno("003", "Antônio Oliveira")]
    cursos = [Curso("001", "Programação"), Curso("002", "Matemática"), Curso("003", "Português")]
    while True:
        i = int(input('''
================Sistema Escolar================
1. Listar todos os alunos cadastrados.
2. Listar todos os cursos cadastrados.
3. Matricular um aluno em um curso.
4. Exibir em quais cursos um aluno está matriculado.
5. Encerrar o programa.
> '''))
        if i == 1:
            #> Listar alunos
            print("\nAlunos:")
            for aluno in alunos:
                print(f"> {aluno.matricula} - {aluno.nome}")
                '''if aluno.cursos == []:
                    print(">> Aluno não está matriculado em curso.")
                else:
                    for curso in aluno.cursos:
                        print(f">> {curso.nome}")'''
        elif i == 2:
            print("\nCursos:")
            for curso in cursos:
                print(f"> {curso.id} - {curso.nome}")
        elif i == 3:
            try:
                found = False
                mat = input("Insira a matrícula do aluno:\n> ")
                for alunop in alunos:
                    if mat == alunop.matricula:
                        print(f"Aluno encontrado: [{alunop.matricula}] - {alunop.nome}")
                        aluno = alunop
                        found = True
                        break
                if found == False:
                    print("Aluno não encontrado.")
                    continue
                found = False
                id = input("Insira o id do curso:\n> ")
                for cursop in cursos:
                    if id == cursop.id:
                        print(f"Curso encontrado: [{cursop.id}] - {cursop.nome}")
                        curso = cursop
                        found = True
                        break
                if found == False:
                    print("Curso não encontrado.")
                    continue
                        
                aluno.matricular(curso)
                    
            except Exception as err:
                print(f"Algo deu errado.\n>>ERRO: {err}")
        elif i == 4:
            try:
                found = False
                mat = input("Insira a matrícula do aluno:\n> ")
                for alunop in alunos:
                    if mat == alunop.matricula:
                        print(f"Aluno encontrado: [{alunop.matricula}] - {alunop.nome}")
                        aluno = alunop
                        found = True
                        break
                if found == False:
                    print("Aluno não encontrado.")
                    continue
                print(f"\nAluno: {aluno.nome}")
                print("Cursos matriculados:")
                for curso in aluno.cursos:
                    print(f"> {curso.nome}")
            except Exception as err:
                print(f"Algo deu errado.\n>>ERRO: {err}")
        elif i == 5:
            break
        
if __name__ == "__main__":
    main()