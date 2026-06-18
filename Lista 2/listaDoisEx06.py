'''
Ex. 6. 
Escreva um programa em Python que simule o controle de
uma sala de cinema. O cinema possui 10 assentos
numerados de 1 a 10, e o programa deve manter uma lista de
ocupação dos assentos (com valores booleanos, onde True
indica ocupado e False indica livre). O usuário poderá
interagir com o sistema por meio de um menu com as
seguintes opções:
1. Reservar um assento
2. Liberar um assento
3. Mostrar mapa de ocupação (exibindo quais assentos
estão ocupados e quais estão livres)
4. Sair
O programa deve impedir a reserva de assentos já ocupados
e a liberação de assentos que já estão livres. Utilizar função.
'''

def reservar(lista:dict):
    livres = [k for k, v in lista.items() if not v]
    print()
    print(f"Assentos disponíveis:\n{str(livres).replace("\'", "")}\n")
    k = input("Qual assento deseja reservar?\n> ")
    if k in livres:
        print("Assento reservado.")
        lista[k] = True
    else:
        print("Assento indisponível ou ocupado.")
    
    return lista
def liberar(lista):
    ocupados = [k for k, v in lista.items() if v]
    print(f"Assentos ocupados:\n{str(ocupados).replace("\'", "")}\n")
    k = input("Qual assento deseja reservar?\n> ")
    if k in ocupados:
        print("Assento liberado.")
        lista[k] = False
    else:
        print("Assento indisponível ou livre.")
        
    return lista
def mostrar_mapa(lista):
    ocupados = [k for k, v in lista.items() if v]
    livres = [k for k, v in lista.items() if not v]
    print(f"Assentos ocupados:\n{str(ocupados).replace("\'", "")}\n")
    print(f"Assentos disponíveis:\n{str(livres).replace("\'", "")}\n")
    return


def ex6():
    import time
    
    assentos = {}
    for i in range(10):
        assentos[str(i+1)] = False
    while True:
        i = int(input('''
=============== Menu de Assentos ===============
Escolha uma opção.

1. Reservar um assento
2. Liberar um assento
3. Mostrar mapa de ocupação
4. Sair

> '''))
        
        if i == 1:
            assentos = reservar(assentos)
            pass
        elif i == 2:
            assentos = liberar(assentos)
            pass
        elif i == 3:
            mostrar_mapa(assentos)
            time.sleep(2)
            pass
        elif i == 4:
            print("Saindo...")
            break
        time.sleep(1)
            

if __name__ == "__main__":
    ex6()