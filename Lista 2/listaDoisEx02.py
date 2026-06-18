'''
Ex. 2.
Faça um programa em Python que simula as operações de
um banco. O programa deve apresentar um menu com as
seguintes opções:
1. Depositar (O programa deve pedir o valor a ser
depositado e somá-lo ao saldo)
2. Sacar (O programa deve pedir o valor a ser sacado e
subtrair do saldo, desde que o valor seja menor ou igual
ao saldo disponível)
3. Consultar Saldo (O programa deve exibir o saldo
atual)
4. Sair (O programa termina)
O programa deve manter um saldo inicial de R$ 1000,00
e permitir ao usuário realizar depósitos e saques até que
ele escolha a opção "Sair".
'''


def ex2():
    import time
    saldo = 1000.00
    while True:
        try:
            i = int(input('''
=============== Menu do Banco ===============
Escolha uma opção.

1 - Depositar
2 - Sacar
3 - Consultar Saldo
4 - Sair

> '''
    ))
            if i == 1:
                #Depositar  
                saldo += float(input("Insira o valor que você deseja depositar:\n> R$ "))
                print("Depósito efetuado com sucesso.")
            elif i == 2:
                #Sacar
                saque = float(input("Insira o valor que deseja sacar.\n> R$ "))
                if saldo >= saque and saque > 0:
                    saldo -= float(input("Insira o valor que deseja sacar.\n> R$ "))
                    print("Saque efetuado com sucesso.")
                else:
                    print("Valor inválido, tente novamente.")
                    
            elif i == 3:
                print(f"O saldo atual é de R${saldo:.2f}")
            else:
                break
            time.sleep(1)  
        except KeyboardInterrupt:
            break     
        except:
            print("\nAlgo deu errado, tente novamente mais tarde.")
            time.sleep(1)  

if __name__ == "__main__":
    ex2()
