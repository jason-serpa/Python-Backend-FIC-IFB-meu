'''
Ex. 3. 
Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy
(Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).
'''
def ex3():
    x = int(input("Insira o valor X\n"))
    y = int(input("Insira o valor Y\n"))

    resultado = 1
    if y != 0:
        for _ in range(y):
            resultado *= x
    print(f"O resultado é {resultado}.")


if __name__ == "__main__":
    ex3()