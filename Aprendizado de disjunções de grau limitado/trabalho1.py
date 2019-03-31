
#NOME: FELIPE ARAUJO MAGALHAES - 378599
#NOME: LUCAS NOLETO PAIVA - 390192
#
#k = 4
#n = 4 # Numero total de variables: x1, x2, ..., xn,
#m = 4

import numpy as np
import itertools as it


def trabalhoAlgoritmoDisjuncoes(n,m,k):
    #FUNCOES DA FUNÇÃO---------------------------------------------------------
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
    
    def todosMonomiosPossiveis():
        # Numero total de variables: x1, x2, ..., xn
        A = [0, 1, -1]
        # U = Todos monomios possiveis
        U = it.product(A, repeat=n)
        U = [list(i) for i in Todos]
        #T é o mais novo conj de monomios sem a ocorrencia de 0 em todos
        T=[]
        for m in U:
            if n-k <= m.count(0)<n:
                T.append(m)
        return T
    
    def verificarClasse(mon,sample):
        for i in range(m):
            for literal in mon:
                if literal<0 and sample[i][-literal-1]==1:
                    if classe[i]==1:
                        return mon
                elif literal>0 and sample[i][literal-1]==0:
                    if classe[i]==1:
                        return mon
                elif literal>0 and sample[i][literal-1]==1:
                    if classe[i]==0:
                        return mon
                elif literal<0 and sample[i][literal-1]==0:
                    if classe[i]==1:
                        return mon
    
    #-------------------------------------------------------------------------------------------------
    
    S = np.random.randint(0, 2, size=(m,n)) #exemplo de amostra
    
    A = [0, 1, -1]
    Todos = it.product(A, repeat=n)
    Todos = [list(i) for i in Todos]
    
    #Todos = todosMonomiosPossiveis()
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
    print('-----------------------------------------')
    print('Representação do monomio conceito:', lista_monomio_conceito)
    print('Amostra:')
    print(S)
    
    #classe = []
    #Aqui foi feito um for pra calcular para cada conj de literais da lista de literais para construir
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
    print('classe:' ,classe)
    
    todosMonomios = todosMonomiosPossiveis()
    #Corro toda a lista de monomios criada para essa tarefa, e as removo da lista de monomios original, criada laaaaa em cima >>TODOS<<
    print('-----------------------------------------')
    print('Monomios para remover a cada iteração:')
    for i in range(len(todosMonomios)):
        monomiosToDelete = (verificarClasse(todosMonomios[i],S))
        print(monomiosToDelete)
        if Todos.count(monomiosToDelete)>0:
            Todos.remove(monomiosToDelete)
    print('Todos os monomios restantes:')
    print(Todos)


#Chamada da funcao, onde a ordem dos parametros sao : trabalhoAlgoritmoDisjuncoes(N,M,K)
#para testar outros valores, apenas substituir os valores nos parametros da função
trabalhoAlgoritmoDisjuncoes(3,3,3)

#Se todo o trabalho estiver correto, nos recomendamos a seguinte trilha sonora para executar o código:
#>>>>>https://www.youtube.com/watch?v=O71fetlkCZo
