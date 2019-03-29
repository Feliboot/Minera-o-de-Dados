## Introducao aa Mineracao de Dados, 2019.1, UFC/DEMA
##
## Gerar todos os monomios de grau 1, 2, e 3
## Cada monomio sera' representado por um tupla
#NOME: FELIPE ARAUJO MAGALHAES - 378599
#NOME: LUCAS NOLETO PAIVA - 390192
#
k = 3
n = 3 # Numero total de variables: x1, x2, ..., xn,
m = 3

import numpy as np
import itertools as it

S = np.random.randint(0, 2, size=(m,n)) #exemplo de amostra

A = [0, 1, -1]
Todos = it.product(A, repeat=n)
Todos = [list(i) for i in Todos]

def achar_classe(mon,sample):
    classe=[]
    for i in range(m):
        c = 1
        for literal in mon:
            if literal<0 and sample[i][-literal-1]==1:
                c = 0
            elif literal>0 and sample[i][literal-1]==0:
                c = 0
        classe.append(c)
    return classe  


# Guardar em M apenas os monomios de grau 1, 2, e 3
M = []
for monomio in Todos:
    c = [abs(v) for v in monomio]
    if 1 <= sum(c) <= 3:
        M.append(monomio)

#print('\n----------------------------------------------------------------\n')
#print('Monomios de grau 1, 2, e 3:')
#print(M)


#criando os monomios conceitos utilizados para gerar a classe
lista_monomio_conceito=[]
for i in range(1,k+1):
    monomio_conceito = []
    for j in range(1,n+1):
        v = np.random.rand()
        if v < 1/3:
            monomio_conceito.append(-j)
        elif v > 2/3:
            monomio_conceito.append(j)
        else:
            pass
    lista_monomio_conceito.append(monomio_conceito)
print('Representacao do monomio conceito:', lista_monomio_conceito)

print('Amostra:')
print(S)

#classe = []
#Aqui fiz um for pra calcular para cada conj de literais da lista de literais para construir
#a classe de maneira concisa/sucinta com os monomios conceito criados.
lista_das_classes=[]
for j in range(0,k):
    lista_das_classes.append(achar_classe(lista_monomio_conceito[j],S))

#convertendo a lista pra matrix pra operar com o any
matrix = np.array(lista_das_classes)
matrix = matrix.T

classe_booleana = [ any(line) for line in matrix ]

classe=[]
for convert in classe_booleana:
    classe.append(int(convert))
print('class:' ,classe)


#Esse pedaço de codigo aqui embaixo é do codigo
#passado em sala pelo professor, poderiamos começar daqui construir o nosso!
# for i in range(m):
#     if classe[i] == 1:
#         for j in range(n):
#             if S[i][j]==1:
#                 #remove de U o elemento -(j+1)
#                 if M.count(-j-1)>0:
#                     M.remove(-j-1)
#             else:
#                 if M.count(j+1)>0:
#                     M.remove(j+1)
#     print(M)
