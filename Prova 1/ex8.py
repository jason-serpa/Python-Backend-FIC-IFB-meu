'''Ex. 8
Crie um algoritmo que:
- Peça o nome do usuário;
- Exiba uma mensagem personalizada: “Olá, [nome]! Bem-vindo(a)!”
Objetivo: entrada e saída com concatenação de string.
> Faça o fluxograma no Flowgorithm
'''
def ex8():
    print(f"Olá, {input("Informe seu nome:\n> ").capitalize()}! Bem-vindo(a)!")
    
if __name__ == "__main__":
    ex8()
