'''
EX. 1 O custo ao consumidor de um carro novo é a soma do custo
de fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que a porcentagem
do distribuidor seja de 12% do preço de fábrica e os impostos
de 30% do preço de fábrica, fazer um programa em Python
para ler o custo de fábrica de um carro e imprimir o custo ao
consumidor.
'''

def main():
    
    precoFab = float(input("Insira o preço de fábrica:\n"))
    
    porcentDistrib = 0.12*precoFab
    porcentImpos = 0.30*precoFab
    custoCons = precoFab + porcentDistrib + porcentImpos

    print(f"O custo do consumidor é de {custoCons:.2f}R$")

    confirm = input("Deseja repetir o programa? Pressione Enter se sim.\n")
    if confirm == "":
        return main()
    else:
        return

main()

