'''Ex. 1. 
Crie um programa em Python que recebe um valor em reais e
o converte para outra moeda. Use um menu para escolher a
moeda de destino:
1. Dólar
2. Euro
3. Libra
4. Iene

O programa deve perguntar o valor em reais e exibir o
valor convertido para a moeda escolhida. Use valores
fictícios para as taxas de conversão:
1 Real = 0.19 Dólar
1 Real = 0.17 Euro
1 Real = 0.15 Libra
1 Real = 25 Ienes
'''

def ex1():
    listagemNomes = (
        ("Dólar", "Dólares"), 
        ("Euro", "Euros"), 
        ("Libra", "Libras"), 
        ("Iene", "Ienes")
    )
    cotacaoReais = {"Dólar": 0.19, "Euro": 0.17, "Libra": 0.15, "Iene": 25}

    i = int(input('''
=============== Menu de Cotação ===============
Escolha uma opção para converter seu dinheiro.

1 - Converter para Dólar
2 - Converter para Euro
3 - Converter para Libra
4 - Converter para Iene

> '''
    ))-1

    valorConvertido = float(input("\nInsira o valor em reais.\n> ")) * \
        float(cotacaoReais[listagemNomes[i][0]])
    if valorConvertido != 1:
        nome = listagemNomes[i][1]
    else:
        nome = listagemNomes[i][0]
    print(f"O valor convertido equivale a {valorConvertido:.2f} {nome.lower()}")

if __name__ == "__main__":
    ex1()



