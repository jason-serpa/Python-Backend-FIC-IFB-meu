'''
EX. 4
Elabore um programa em Python que leia as duas notas de
prova (P1 e P2) e duas notas de trabalho (T1 e T2) e
posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não
aprovado’ dependendo dos valores obtidos, conforme as
regras de cálculo definidas a seguir:
• Média de provas: MP = (P1 + P2)/2
• Média de trabalhos: MT = (T1 + T2)/2
• Média final: MF = 0,8MP + 0,2MT
• Situação:
◦ Se MF ≥ 6,0 → aprovado
◦ Se MF < 6,0 → não aprovado


'''

def main():
    p1 = float(input("Insira o valor da primeira nota da prova:\n"))
    p2 = float(input("Insira o valor da segunda nota da prova:\n"))
    t1 = float(input("Insira o valor da primeira nota do trabalho:\n"))
    t2 = float(input("Insira o valor da primeira nota do trabalho:\n"))

    mp = (p1+p2)/2
    mt = (t1+t2)/2
    mf = (0.8*mp)+(0.2*mt)

    if mf >=6:
        print("Está aprovado.")
    else:
        print("Não está aprovado.")
    
    confirm = input("Deseja repetir o programa? Pressione Enter se sim.\n")
    if confirm == "":
        return main()
    else:
        return

main()

