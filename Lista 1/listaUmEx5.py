'''
EX.5
Faça um programa em Python que leia a temperatura em
graus Celsius e determine a classificação da temperatura:
• Menor que 0°C: Frio extremo
• De 0°C a 10°C: Frio
• De 11°C a 25°C: Ameno
• De 26°C a 35°C: Quente
• Maior que 35°C: Muito quente


'''

def main():
    temp = float(input("Qual a temperatura atual?\n"))
    if temp<0:
        print("Está um frio extremo!")
    
    elif temp<=10:
        print("Está frio.")
    
    elif temp<=25:
        print("Está ameno.")
    
    elif temp<=35:
        print("Está quente!")
    
    else:
        print("Está muito quente!")
    
    confirm = input("Deseja repetir o programa? Pressione Enter se sim.\n")
    if confirm == "":
        return main()
    else:
        return

main()

