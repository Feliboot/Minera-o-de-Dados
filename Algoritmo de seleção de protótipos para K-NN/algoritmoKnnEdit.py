#Nome:FELIPE ARAUJO MAGALHAES	Matrícula:378599
#Nome:LUCAS NOLETO PAIVA		Matrícula:390192
#

import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine


#------------------------------------------------------------------------------
# Numero de vizinhos
K = [2,3,5]


S = load_wine()

accKnnGeral=[]
accEditKnnGeral=[]
#dados agora gerados, vamos utilizar knn 
print('Usando dataset wine:')
for num_vizinhos in K:
    for j in range (1,11):
        accKnn=[]
        
        x_train, x_test, y_train, y_test = train_test_split(
               S.data, S.target , test_size=0.33)
        
        neigh = KNeighborsClassifier(num_vizinhos)
        neigh.fit(x_train, y_train)
        y_pred = neigh.predict(x_test)
        accKnn.append(accuracy_score(y_test,y_pred))

        print("Data set na partição {0}, usando KNN(scikitLearn), valor de accuracy para k ={1}" .format(j,num_vizinhos))
        print(accKnn)
        accKnnGeral.append(accKnn)
        #estou adicionando aqueles que foram classificados incorretamente por S ao S_linha, ou seja, algoritmo 2 do livro 
        #sobre edit knn
        S_linha_x = []
        S_linha_classe=[]
        for i in range(len(y_test)):
            if y_pred[i] != y_test[i]:
                S_linha_x.append(x_train[i])
                S_linha_classe.append(y_test[i])

        print('------------------------------------------------------------------------------')
#         print(S_linha_x,end="\n\n")
#         print(S_linha_classe)

        x_train, x_test, y_train, y_test = train_test_split(
           S_linha_x, S_linha_classe , test_size=0.33)

        accEditKnn=[]

        neigh = KNeighborsClassifier(K[1])
        neigh.fit(x_train, y_train)
        y_pred = neigh.predict(x_test)
        accEditKnn.append(accuracy_score(y_test,y_pred))

        print("Valor de accuracy do edit Knn para k = {}".format(num_vizinhos))
        print(accEditKnn)
        accEditKnnGeral.append(accEditKnn)
        print('------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------')

        
#print de accuracy de todos os knn's feitos tanto no S original como no S'         
#Print(accKnnGeral)
#print(accEditKnnGeral)