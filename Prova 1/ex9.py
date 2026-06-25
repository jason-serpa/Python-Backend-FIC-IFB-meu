'''Ex. 9.
Crie um algoritmo que:
1. Solicite ao usuário um número inteiro.
2. Envie esse número para uma função chamada CalcularQuadrado, que retorne
o quadrado do número.
3. Mostre o resultado na tela.
4. Faça o fluxograma no Flowgorithm
'''
def CalcularQuadrado(num):
    return num*num
def ex9():
    num = int(input("Insira um número inteiro.\n> "))
    print(f"O quadrado do número {num} é {CalcularQuadrado(num)}")

if __name__ == "__main__":
    ex9()
