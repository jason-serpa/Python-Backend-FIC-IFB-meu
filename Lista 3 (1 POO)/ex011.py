
'''11. Desenvolva um sistema para gerenciar veículos de transporte
público em uma cidade inteligente. Crie uma classe abstrata
VeiculoTransporte, com os atributos placa e
capacidadePassageiros, e um método abstrato
calcularCustoOperacional() que retorna o custo por
quilômetro. Crie as subclasses Onibus, com o atributo
consumoPorKm (litros/km), e Metro, com
consumoEnergiaPorKm (kWh/km). Cada uma deve
implementar o cálculo do custo com valores fictícios: R$ 6,00
por litro de diesel e R$ 0,80 por kWh. Na função principal,
permita criar objetos dos dois tipos e exibir os custos
operacionais usando polimorfismo. Implemente tratamento de
exceções para validar os dados de entrada: placa não pode
ser vazia, e os valores numéricos devem ser positivos.
'''

from abc import ABC, abstractmethod
class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidadePassageiros):
            self.placa = placa
            self.capacidadePassageiros = capacidadePassageiros

    @abstractmethod
    def calcularCustoOperacional(self, ):
          pass
# 30 em um KM, considerando que o custo por litro é 6 reais, custo operacional será 30*6, ou (consumo*custo)
class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoPorKm):
        VeiculoTransporte.__init__(self, placa=placa, capacidadePassageiros=capacidadePassageiros)
        self.consumoPorKm = consumoPorKm
        self.tipo = "Ônibus"
        
    def calcularCustoOperacional(self):
        self.custo = self.consumoPorKm*6
        print(">>> O custo operacional do veículo é de:", self.custo, "R$")
    
class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoEnergiaPorKm):
        VeiculoTransporte.__init__(self,placa=placa, capacidadePassageiros=capacidadePassageiros)
        self.consumoEnergiaPorKm = consumoEnergiaPorKm
        self.tipo = "Metrô"
        
    def calcularCustoOperacional(self):
        self.custo = self.consumoEnergiaPorKm*0.8
        print(">>> O custo operacional do veículo é de:", self.custo, "R$")



'''
Na função principal,
permita criar objetos dos dois tipos e exibir os custos
operacionais usando polimorfismo. Implemente tratamento de
exceções para validar os dados de entrada: placa não pode
ser vazia, e os valores numéricos devem ser positivos.
'''
def main():

    veiculos = []
    while True:
        i = int(input('''
================Consumos de Veículos================
1. Cadastrar Veículo
2. Exibir custos operacionais
3. Sair do programa
> '''))
        if i == 1:
            try:
                placa = input("Insira a placa do veículo:\n> ")
                if placa == "":
                    raise ValueError("Informe uma placa válida.")
                cap = input("Insira a capacidade de passageiros:\n")
                if cap.isnumeric() == False or int(cap) < 1:
                    raise ValueError("Informe uma quantidade válida.")
                cap = int(cap)
                escolha = int(input("O veículo é um metrô ou ônibus?\n1- Metrô\n2- Ônibus\n> "))
                if escolha == 1:
                    cons = float(input("Qual o consumo de energia por Km?\n> "))
                    veiculos.append(Metro(placa=placa, capacidadePassageiros=cap, consumoEnergiaPorKm=cons))
                elif escolha == 2:
                    cons = float(input("Qual o consumo de gasolina por Km?\n> "))
                    veiculos.append(Onibus(placa=placa, capacidadePassageiros=cap, consumoPorKm=cons))
                else:
                    print("Escolha inválida")
                    raise IndexError("Escolha um número válido")

                print("Veículo\"", placa, "\" adicionado com sucesso.")
            except Exception as err:
                print(">>> ERRO:", err)
            
        if i == 2:
            print("Custo operacional por veículo:")
            for veic in veiculos:
                print(">", veic.placa)
                print(">> Tipo:", veic.tipo)
                print(">> Capacidade do veículo:", veic.capacidadePassageiros)
                if type(veic) == Onibus:
                    print(">> Consumo por KM:", veic.consumoPorKm, "kWh/km")
                elif type(veic) == Metro:
                    print(">> Consumo por KM:", veic.consumoEnergiaPorKm, "kWh/km")
                veic.calcularCustoOperacional()
                
                print()
        if i == 3:
            break
        

    return 
    
if __name__ == "__main__":
    main()