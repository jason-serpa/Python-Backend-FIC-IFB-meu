'''
EX. 2
Faça um programa em Python que leia dois números inteiros
quaisquer para as variáveis A e B, efetue a troca dos valores
de forma que A passe a armazenar o valor de B e que B
passe armazenar o valor de A e que imprima os valores
trocados.

'''
def main():
    num1 = str(input("Insira o primeiro número:\n"))
    num2 = str(input("Insira o segundo número:\n"))
    listaNums = [num1, num2]
    num1 = listaNums[1]
    num2 = listaNums[0]
    print("A primeira variável está com o valor de: " + num1 + \
          "\nE a segunda está com o valor de: " + num2)
        
    confirm = input("Deseja repetir o programa? Pressione Enter se sim.\n")
    if confirm == "":
        return main()
    else:
        return

main()

