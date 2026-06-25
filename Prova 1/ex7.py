'''Ex. 7
Faça um algoritmo que:
- Solicite um número ao usuário;
- Informe se o número é par ou ímpar.

> Faça o fluxograma no Flowgorithm
'''
def ex7():
    try:
        if int(input("Insira um número:\n> ")) % 2 == 0:
            print("O valor é par.")
        else:
            print("O valor é ímpar.")
    except ValueError:
        print("Valor inválido, tente novamente.\n")
        return ex7()
    

if __name__ == "__main__":
    ex7()