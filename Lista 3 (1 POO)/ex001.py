'''
1. Elabore um programa em Python orientado a objetos que leia
um número n (o número de termos de uma progressão
aritmética), a1 (o primeiro termo da progressão) e r (razão) e
escreva todos os termos dessa progressão, bem como a
soma dos elementos (Fórmulas da P.A.: an = a1 + r x (n – 1) e
S = n * (a1 + an) / 2).
'''

class Numero:
    def progressao(self, n, a1, r):
        lista = ()
        for num in range(a1, n+1, r):
            print(num)
            lista += (num, )
        return lista
    
    def somar(self, numeros):
        resultado = 0
        for num in numeros:
            resultado += num
        return resultado



            

# n= Quantidade de números
# a1 = Número inicial
# r= Razão

soma = Numero().progressao(n=10, a1=2, r=2)
print()
print(Numero().somar(soma))

