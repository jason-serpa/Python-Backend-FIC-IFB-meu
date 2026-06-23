'''Ex. 8. 
Uma universidade está organizando os dados de participação
dos alunos em dois eventos acadêmicos: uma palestra sobre
Inteligência Artificial e um workshop de Programação em
Python. Os dados de presença são armazenados em dois
conjuntos distintos: palestra_ia e workshop_python, contendo
os nomes dos alunos que participaram de cada evento.
Escreva um programa em Python com o seguinte menu
interativo:
1. Adicionar aluno a um evento: O programa deve perguntar
o nome do aluno e em qual evento ele participou (IA ou
Python) e adicionar o nome ao conjunto correspondente.
2. Mostrar alunos que participaram de ambos os eventos:
Exiba os nomes que aparecem nos dois conjuntos
(interseção).
3. Mostrar alunos que participaram somente da palestra de
IA: Exiba os nomes que estão no conjunto da palestra, mas
não no workshop (diferença).
4. Mostrar alunos que participaram de pelo menos um evento:
Exiba a união dos dois conjuntos, sem repetições.
5. Verificar participação de um aluno: Solicite o nome de um
aluno e diga se ele participou de ambos, somente um ou
nenhum dos eventos.
6. Sair
O programa deve funcionar em laço até que o usuário
escolha a opção de sair. Utilize operações com conjuntos
(union, intersection, difference) para resolver as tarefas.
Utilizar função.'''

def adicionar(IA, PP):
    from time import sleep
    aluno = input("Insira o nome do aluno:\n> ").upper()
    foiIA = input("\nO aluno participou do evento sobre Inteligência Artificial?\n1- Sim\n2- Não\n> ")
    if int(foiIA) == 1:
        print(f"O aluno {aluno} será adicionado na lista do evento sobre Inteligência Artificial.\n")
        sleep(1)
        IA.add(aluno)
    foiPP = input("\nO aluno participou do evento sobre Programação em Python?\n1- Sim\n2- Não\n> ")
    if int(foiPP) == 1:
        print(f"O aluno {aluno} será adicionado na lista do evento sobre Programação em Python.\n")
        sleep(1)
        PP.add(aluno)
    return IA, PP

def mostrar_ambos(IA, PP):
    intersec = IA & PP
    print("\nAlunos que participaram dos dois eventos:\n")
    for aluno in intersec:
        print(f"- {aluno}")
    return

def mostrar_IA(IA, PP):
    diferenca = IA - PP
    print("Alunos que participaram somente no evento sobre Inteligência artificial:\n")
    for aluno in diferenca:
        print(f"- {aluno}")
    return

def mostrar_um(IA, PP):
    uniao = IA | PP
    print("Alunos que participaram de ao menos um evento:\n")
    for aluno in uniao:
        print(f"- {aluno}")
    return

def verificar_part(IA, PP):
    nome = input("Insira o nome do aluno:\n> ").upper()
    if nome not in (IA | PP):
        print(f"O aluno {nome} não participou de nenhum evento.")
        return
    elif nome in IA & PP:
        print("O aluno participou dos dois eventos.")
        return
    elif nome in IA - PP:
        print("O aluno participou do evento sobre Inteligência Artificial")
        return
    elif nome in PP - IA:
        print("O aluno participou do evento sobre Programação em Python")
        return
    elif nome in IA:
        print(f"O aluno participou do evento")
        return
    else:
        print("Erro, tente novamente.\n\n")
        return verificar_part(IA, PP)
    



def ex8():
    from time import sleep
    IA = set() 
    PP = set()
    while True:
        i = int(input('''
=============== Dados de Presença ===============
Escolha uma opção.


1. Adicionar aluno a um evento
2. Mostrar alunos que participaram de ambos os eventos
3. Mostrar alunos que participaram somente da palestra de IA
4. Mostrar alunos que participaram de pelo menos um evento
5. Verificar participação de um aluno
6. Sair

> '''))
        
        if i == 1:
            IA, PP = adicionar(IA, PP)
            pass
        elif i == 2:
            mostrar_ambos(IA, PP)
            pass
        elif i == 3:
            mostrar_IA(IA, PP)
            pass
        elif i == 4:
            mostrar_um(IA, PP)
            pass
        elif i == 5:
            verificar_part(IA, PP)
            pass
        elif i == 6:
            print("Saindo...")
            break
        sleep(1)
            

if __name__ == "__main__":
    ex8()