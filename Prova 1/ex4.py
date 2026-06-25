'''Ex. 4 
Faça um algoritmo que:
- Solicite uma palavra ao usuário;
- Conte quantas vogais existem na palavra;
- Mostre na tela o total de vogais.
'''
def ex4():
    num = 0
    vogais = ["A", "E", "I", "O", "U"]
    palavra = input("Insira uma palavra.\n> ").upper()
    vogaisEncontradas = []
    for letra in range(len(palavra)):
        if palavra[letra] in vogais:
            vogaisEncontradas.append(palavra[letra])

    print(f"O total de vogais é {len(vogaisEncontradas)}")

if __name__ == "__main__":
    ex4()