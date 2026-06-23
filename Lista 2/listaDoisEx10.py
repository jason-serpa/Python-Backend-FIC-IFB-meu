'''
Ex. 10. 
Você foi contratado para desenvolver um sistema simples
para gerenciar um campeonato de futebol. O sistema deve
usar um dicionário onde as chaves são os nomes dos times e
os valores são os pontos conquistados. O programa deve
apresentar o seguinte menu:
1. Adicionar time: permite cadastrar um novo time com 0
pontos iniciais.
2. Registrar resultado de partida: o usuário informa os nomes
de dois times e o resultado da partida (quantidade de gols de
cada time). O programa atualiza os pontos dos times: 3
pontos para o vencedor, 1 ponto para empate, 0 para o
perdedor.
3. Mostrar classificação: exibe a lista dos times e seus
pontos, ordenada do maior para o menor número de pontos.
4. Remover time: permite remover um time da competição.
5. Sair
O programa deve funcionar em loop até o usuário escolher
sair. Utilizar função.
'''

def adicionar(sistema):
    equipe = input("Insira o nome do time.\n> ").upper()
    sistema.update({equipe: 0})
    return sistema

def registrar(sistema:dict):
    print(len(sistema.keys()))
    if len(sistema.keys())<2:
        print(f"O número atual de times é apenas {len(sistema.keys())}, é necessário ao menos dois times.")
        return sistema
    equipeUm = input("Insira o nome da primeira equipe:\n> ").upper()
    placarUm = int(input(f"Quantos gols a {equipeUm} realizou no jogo?\n> "))
    equipeDois = input("Insira o nome da segunda equipe:\n> ").upper()
    placarDois = int(input(f"Quantos gols a {equipeDois} realizou no jogo?\n> "))
    print()
    if placarUm>placarDois:
        sistema[equipeUm] += 3
        print(f"{equipeUm} venceu.\n> +3 Pontos\n")

    elif placarUm<placarDois:
        print(f"{equipeDois} venceu.\n> +3 Pontos\n")
        sistema[equipeDois] += 3

    elif placarUm==placarDois:
        print(f"Empate entre os times {equipeUm} e {equipeDois}\n> +1 Ponto")
        sistema[equipeUm] += 1
        sistema[equipeDois] += 1
    return sistema

def mostrar(sistema: dict):
    from time import sleep
    if sistema == {}:
        print("Não há times no sistema.")
        sleep(1)
        return
    sistemaOrdenado = dict(sorted(sistema.items(), key=lambda ordem:ordem[1], reverse=True))
    print("\nPlacar atual:")
    for equipe in sistemaOrdenado:
        print(f"- {equipe}: {sistemaOrdenado[equipe]} pontos")
    sleep(2)

    return

def remover(sistema:dict):
    equipe = input("Insira o time que deseja remover.\n> ").upper()
    sistema.pop(equipe)
    print(f"Equipe {equipe} removida do sistema.")
    return sistema


def ex10():
    import time
    sistema = dict()
    while True:
        i = int(input('''
=============== Gerenciador Futebol ===============
Escolha uma opção.

1. Adicionar time
2. Registrar resultados de partida
3. Mostrar classificação
4. Remover time
5. Sair

> '''))
        
        if i == 1:
            sistema = adicionar(sistema)
            pass
        elif i == 2:
            sistema = registrar(sistema)
            pass
        elif i == 3:
            mostrar(sistema)
            pass
        elif i == 4:
            sistema = remover(sistema)
            pass
        elif i == 5:
            print("Saindo...")
            break
        time.sleep(1)
            

if __name__ == "__main__":
    ex10()