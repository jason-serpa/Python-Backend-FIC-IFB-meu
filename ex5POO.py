'''Você foi contratado para desenvolver um sistema para gerenciar
informações e estatísticas dos clubes participantes da Copa do Mundo
de Clubes da FIFA. 
Para isso, implemente uma classe abstrata chamada
ClubeParticipante com os atributos nome, pais, confederacao,
ranking_fifa, gols_marcados e vitorias, 
incluindo um método concreto exibir_dados() para mostrar os 
dados do clube, e métodos abstratos
- calcular_desempenho() — que deve calcular um índice baseado na
fórmula específica da confederação (para clubes da UEFA: desempenho
= vitórias × 3 + gols marcados × 0,5; para clubes da CONMEBOL:
desempenho = vitórias × 3 + gols marcados × 0,7) — e
- gerar_relatorio_tecnico(), que deve exibir as informações básicas do
clube junto com o desempenho calculado. Crie duas subclasses
concretas, ClubeUEFA e ClubeCONMEBOL, que implementem esses
métodos de acordo com as regras definidas, e teste a aplicação criando
instâncias de cada tipo, demonstrando o uso de abstração, herança e
polimorfismo em Python.
'''

from abc import ABC, abstractmethod

class ClubeParticipante(ABC):
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa        
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias        
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Confederação: {self.confederacao}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
        print(f"Gols marcados: {self.gols_marcados}")
        print(f"Vitórias: {self.vitorias}")

    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass

class ClubeUEFA(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.5 
    
    def gerar_relatorio_tecnico(self):
        print("-"*10, end="")
        print("RELATÓRIO TÉCNICO (UEFA)", end="")
        print("-"*10)
        self.exibir_dados()
        print(f"\nÍndice de desempenho: {self.calcular_desempenho():.2f}", end="\n\n")
        return
class ClubeCONMEBOL(ClubeParticipante):
    def calcular_desempenho(self):
        return self.vitorias * 3 + self.gols_marcados * 0.7 
    
    def gerar_relatorio_tecnico(self):
        print("-"*10, end="")
        print("RELATÓRIO TÉCNICO (CONMEBOL)", end="")
        print("-"*10)
        self.exibir_dados()
        print(f"\nÍndice de desempenho: {self.calcular_desempenho():.2f}", end="\n\n")
        return
    

if __name__ == "__main__":
    # Instanciando clubes concretos
    clube1 = ClubeUEFA(
        nome="FC Barcelona",
        pais="Espanha",
        confederacao="UEFA",
        ranking_fifa=1,
        gols_marcados=18,
        vitorias=6
    )

    clube2 = ClubeUEFA(
        nome="Real Madrid",
        pais="Espanha",
        confederacao="UEFA",
        ranking_fifa=2,
        gols_marcados=15,
        vitorias=5
    )

    clube3 = ClubeCONMEBOL(
        nome="Flamengo",
        pais="Brasil",
        confederacao="CONMEBOL",
        ranking_fifa=8,
        gols_marcados=14,
        vitorias=5
    )

    clube4 = ClubeCONMEBOL(
        nome="Boca Juniors",
        pais="Argentina",
        confederacao="CONMEBOL",
        ranking_fifa=12,
        gols_marcados=10,
        vitorias=4
    )

    clubes = [clube1, clube2, clube3, clube4]

    print("########## RELATÓRIOS DE TODOS OS CLUBES ##########")
    for clube in clubes:
        clube.gerar_relatorio_tecnico()

    print("\n########## COMPARATIVO DE DESEMPENHO ##########")
    for clube in clubes:
        print(f"{clube.nome} ({clube.confederacao}): {clube.calcular_desempenho():.2f} pontos")