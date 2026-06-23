'''
Ex. 9. 
Uma livraria quer controlar seu estoque usando um dicionário
onde as chaves são os títulos dos livros e os valores são a
quantidade disponível em estoque. Implemente um programa
com as seguintes funcionalidades:
1. Adicionar um livro ao estoque: o usuário informa o título e a
quantidade (se o livro já existir, some a quantidade nova à
existente).
2. Remover unidades de um livro: o usuário informa o título e
a quantidade a remover; o programa deve atualizar o estoque
e avisar se o estoque ficar zerado ou se o livro não existir.
3. Consultar quantidade de um livro: o usuário digita o título e
o programa mostra a quantidade disponível ou informa que o
livro não está no estoque.
4. Mostrar todos os livros com suas quantidades ordenados
alfabeticamente.
5. Sair
O programa deve repetir o menu até que o usuário escolha
sair. Utilizar função.
'''

def adicionar(estoque:dict):
    from time import sleep
    livro = input("Insira o nome do livro que deseja adicionar:\n> ").upper()
    quant = int(input("Insira a quantidade de livros:\n> "))
    if livro in estoque:
        print("Livro já existente, adicionando quantidade...")
        estoque[livro] = estoque[livro] + 1
        sleep(1)
        return estoque
    
    print("Adicionando livro...")
    estoque.update({livro: quant})
    sleep(1)
    return estoque


def remover(estoque: dict):
    livro = input("Insira o nome do livro que deseja remover:\n> ").upper()
    quant = int(input("Insira a quantidade de livros:\n> "))

    if livro not in estoque:
        print("Livro não encontrado no estoque.")
        return estoque

    if estoque[livro]-quant <= -1:
        print(f"Quantidade inválida, há apenas {estoque[livro]} livros disponíveis.")
        i = input('''
Deseja alterar a quantidade?
1- Sim, alterar quantidade.
2- Não, manter quantidade.''')
        if i == 1:
            return remover(estoque)
        return estoque
    
    estoque[livro] -= quant
    if quant>1:
        print(f"Foram removidos {quant} livros da lista.")
    else:
        print(f"Foi removido um livro da lista.")
    
    if estoque[livro] == 0:
        print("Livro esgotado.")
        estoque.pop(livro)
        return estoque
    return estoque


def consultar(estoque: dict):
    livro = input("Insira o nome do livro:\n> ").upper()
    if livro not in estoque:
        print(f"Livro \"{livro}\" não encontrado.")
        return
    
    if estoque[livro] > 1:
        print(f"Há {estoque[livro]} unidades do livro {livro} na lista.")
    else:
        print("Há apenas uma unidade do livro na lista.")
    return

def mostrar(estoque: dict):
    estoqueOrdenado = dict(sorted(estoque.items()))
    print("Livros do estoque:")
    for livro in estoqueOrdenado.keys():
        print(f"- {livro}: {estoqueOrdenado[livro]} unidades") 
    return




def ex9():
    import time
    
    estoque = dict()
    
    while True:
        i = int(input('''
=============== Controle de Estoque ===============
Escolha uma opção.

1. Adicionar um livro ao estoque
2. Remover unidades de um livro
3. Consultar quantidade de um livro
4. Mostrar todos os livros com suas quantidades
   ordenadas alfabeticamente
5. Sair

> '''))
        
        if i == 1:
            estoque = adicionar(estoque)
            pass
        elif i == 2:
            estoque = remover(estoque)
            pass
        elif i == 3:
            consultar(estoque)
            pass
        elif i == 4:
            mostrar(estoque)
            pass
        elif i == 5:
            print("Saindo...")
            break
        time.sleep(1)
            

if __name__ == "__main__":
    ex9()