'''
Ex. 7. 
Uma escola aplicou provas em várias turmas e deseja
registrar as maiores notas obtidas por seus alunos. Cada
nota é representada por uma tupla no formato:
(nome_do_aluno, nota, disciplina). Escreva um programa
com o seguinte menu interativo:
1. Adicionar nota: o usuário deve informar o nome do aluno,
a nota (float) e a disciplina, e esses dados devem ser
adicionados como uma nova tupla à lista.
2. Mostrar melhor aluno por disciplina: para cada disciplina
presente na lista, exiba o nome do aluno com a maior nota.
3. Consultar notas por aluno: o usuário digita o nome de um
aluno e o programa mostra todas as notas dele, com a
respectiva disciplina.
4. Exibir notas ordenadas (decrescente): mostre todas as
tuplas da lista ordenadas da maior para a menor nota, no
formato (nota, nome_do_aluno, disciplina).
5. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Use tuplas para armazenar as notas
e manipule-as sem alterar sua estrutura original. Utilizar
função.
'''


# aluno = (nome: str, nota: float, disciplina: str)

# 1. Adicionar nota: o usuário deve informar o nome do aluno,
# a nota (float) e a disciplina, e esses dados devem ser
# adicionados como uma nova tupla à lista.
# 2. Mostrar melhor aluno por disciplina: para cada disciplina
# presente na lista, exiba o nome do aluno com a maior nota.
# 3. Consultar notas por aluno: o usuário digita o nome de um
# aluno e o programa mostra todas as notas dele, com a
# respectiva disciplina.
# 4. Exibir notas ordenadas (decrescente): mostre todas as
# tuplas da lista ordenadas da maior para a menor nota, no
# formato (nota, nome_do_aluno, disciplina).
# 5. Sair
def adicionar(alunos):
    '''Adicionar nota'''

    temp = ((input("Insira o nome do aluno\n> ").upper(), float(input("Insira a nota do aluno\n> ")), input("Insira a disciplina do aluno\n> ").upper()))
    # temp = ("JOSÉ", "7.40", "QUÍMICA")
    alunos = alunos + (temp,)
    return alunos


def mostrar(alunos):
    '''Mostrar melhor aluno por disciplina'''
    disciplinas = []
    melhorAluno = None
    melhoresAlunos = []
    for aluno in alunos:
        if aluno[2] not in disciplinas:
            disciplinas.append(aluno[2])
    
    
    for disciplina in disciplinas:
        #print(disciplina)
        for aluno in alunos:
            if disciplina in aluno[2]:
                print(f"Aluno de {disciplina}: {aluno[0]}")
                if melhorAluno == None:
                    melhorAluno = [aluno[0], aluno[1]]
                else:
                    if melhorAluno[1] < aluno[1]:
                        melhorAluno = [aluno[0], aluno[1]]
    print(f"Melhor aluno: {melhorAluno}")

    #for disciplina in disciplinas:
        
    return


def consultar(alunos):
    '''Consultar notas por aluno'''
    return


def exibir(alunos):
    '''Exibir notas ordenadas'''
    return




def ex7():
    from time import sleep
    alunos = ()
    while True:
        i = int(input('''
=============== Gerenciador de Alunos ===============
Escolha uma opção.

1 - Adicionar nota
2 - Mostrar melhor aluno por disciplina
3 - Consultar notas por aluno
4 - Exibir notas ordenadas
5 - Sair

> '''))
        
        if i == 1:
            alunos = adicionar(alunos)
        elif i == 2:
            mostrar(alunos)
        elif i == 3:
            consultar(alunos)
        elif i == 4:
            exibir(alunos)
        elif i == 5:
            print("Saindo...")
            break
        
            
        sleep(1)
            

if __name__ == "__main__":
    ex7()