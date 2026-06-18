
'''
Ex. 4. 
Faça um programa em Python que imprima todos múltiplos de
x, entre 1 e 100, onde x é um número informado pelo usuário.
Utilizar função.
'''
def encontrar_multiplos(x):
    divisiveis = []
    for i in range(101):
        if i % x == 0 and i != 0:
            divisiveis.append(i)
    divString = str(divisiveis).replace("[", "").replace("]", "")
    print(f"Os números divisíveis por {x} são:\n{divString}")

def ex4():
    encontrar_multiplos(int(input("Insira um número:\n> ")))
    
if __name__ == "__main__":
    ex4()
