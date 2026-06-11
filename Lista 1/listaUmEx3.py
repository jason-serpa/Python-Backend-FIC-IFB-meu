'''
EX. 3
Faça um programa que peça o tamanho de um arquivo para
download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).


'''
def main():
    tamArq = float(input("Insira o tamanho do arquivo, em MB.\n"))
    velInt = float(input("Qual a velocidade da internet?\n"))
    print(f"O tempo aproximado de Download é de: {(tamArq/velInt)/60:.2f} minutos.")
    
    
    confirm = input("Deseja repetir o programa? Pressione Enter se sim.\n")
    if confirm == "":
        return main()
    else:
        return

main()

