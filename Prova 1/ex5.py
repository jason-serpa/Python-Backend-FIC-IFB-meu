'''Ex. 5. 
Crie um algoritmo que:
- Solicite ao usuário um número inteiro;
- Divida 10 por esse número;
- Se o usuário digitar 0 ou um valor inválido, mostre uma mensagem de erro e solicite novamente.

> Faça o fluxograma no Flowgorithm
'''
def ex5():
    try:
        num = int(input("Digite um número inteiro:\n> "))
        if num == 0:
            raise ValueError
    except ValueError:
        print("Valor inválido, tente novamente")
        return ex5()
    print(f"Resultado de {num}/10: {num/10}")

if __name__ == "__main__":
    ex5()