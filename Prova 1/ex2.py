'''Ex. 2 
Crie um algoritmo com um menu que permita ao usuário:
1. Inserir um nome em uma lista.
2. Listar os nomes adicionados.
3. Sair do programa.
O programa deve repetir o menu até o usuário escolher a opção de sair.
'''
def inserir(banco):
    banco.append(input("Insira o nome que deseja adicionar:\n> ").upper())
    
    return banco

def listar(banco):
    from time import sleep
    print("Os nomes encontrados no banco são:")
    for nome in banco:
        print(f"- {nome}")
    sleep(2)
    return

def ex2():
    banco = []
    while True:
        i = int(input('''
=============== Banco de Nomes ===============
Escolha uma opção:
1. Inserir um nome em uma lista.
2. Listar os nomes adicionados.
3. Sair do programa.
> '''))
        
        match i:
            case 1:
                banco = inserir(banco)
            case 2:
                listar(banco)
            case 3:
                return
            case _:
                print("Valor inválido.")

            
if __name__ == "__main__":
    ex2()