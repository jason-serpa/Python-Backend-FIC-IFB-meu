'''Ex. 1 
Crie um algoritmo que:
- Solicite o nome de um aluno e duas notas (de 0 a 10);
- Calcule a média aritmética;
- Mostre o nome do aluno e a situação: "Aprovado" (média ≥ 7), "Recuperação" (entre 5 e 7) ou "Reprovado" (média < 5).
'''
def ex1():
    from time import sleep
    nome = input("Insira o nome do aluno:\n> ").upper()
    media = (float(input("Insira a primeira nota do aluno\n> ")) + float(input("Insira a segunda nota do aluno:\n> ")))/2

    print(f"A média do aluno(a) \"{nome}\" é {media:.2f}, se encontra na situação:\n")
    if media>=7:
        print("Aprovado(a)")
        return
    elif media>=5:
        print("Recuperação")
        return
    elif media>=0:
        print("Reprovado(a)")
        return
    else:
        print("Valor inválido, executando novamente...")
        sleep(1)
        return ex1()

if __name__ == "__main__":
    ex1()


