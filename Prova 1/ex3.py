'''Ex. 3 
Implemente um algoritmo que:
- Inicie com saldo de R$ 500.
- Permita ao usuário:
1. Ver saldo
2. Sacar valor (verificando se há saldo suficiente)
3. Depositar valor
4. Sair
Use estruturas de decisão e laço de repetição.
'''

def ver_saldo(saldo):
    
    print(f"Saldo atual:\n> R${saldo:.2f}")
    return
def sacar(saldo):
    saque = float(input("Insira o valor que deseja sacar:\n> "))
    confirm = int(input(f"\nTem certeza que deseja sacar R${saque:.2f}?\n1- Sim\n2- Não\n> "))
    if confirm == 1 and saldo>=saque:
        print("Saque efetuado.")
        saldo -= saque
    elif saldo<saque:
        print("Saldo insuficiente.")
    return saldo
def depositar(saldo):
    deposito = float(input("Insira o valor que deseja depositar:\n> "))
    confirm = int(input(f"\nTem certeza que deseja depositar R${deposito:.2f}?\n1- Sim\n2- Não\n> "))
    if confirm == 1:
        print("Depósito efetuado.")
        saldo += deposito
    return saldo


def ex3():
    from time import sleep
    saldo = 500.0
    while True:
        i = int(input('''
=============== Caixa Eletrônico ===============
Escolha uma opção:
1. Ver saldo
2. Sacar valor (verificando se há saldo suficiente)
3. Depositar valor
4. Sair
> '''))
        
        match i:
            case 1:
                ver_saldo(saldo)
            case 2:
                saldo = sacar(saldo)
            case 3:
                saldo = depositar(saldo)
            case 4:
                return
        sleep(1)

            
if __name__ == "__main__":
    ex3()