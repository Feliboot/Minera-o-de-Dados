#Felipe Araujo - 378599
#Lucas Noleto - 

import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RepeatedKFold,\
    RepeatedStratifiedKFold, cross_val_score
from sklearn.base import BaseEstimator
#------------------------------------------------------------------------------

class ClassificadorComAjuste(BaseEstimator):
    '''
    ClassificadorComAjuste:
        clf = ClassificadorComAjuste()
        Classificador com ajustes automáticos, onde o mesmo retorna o modelo
        com melhor acurácia de treinamento, utilizando validação cruzada para
        isso.

    '''
    def __init__(self):
        # Atribui um valor padrao para a previsao
        # O valor real deste atributo sera' detectado no metodo 'fit'
        self.__classe_prevista = 0
      
        
        pass

    '''
    fit(X, y):
    Detecta e armazena o melhor valor do parametro passado para o modelo.
    '''
    def fit(self, X, y,p,l):
        self.__p = p
        self.__l = l
        
        parametros = dict()
        parametros[str(p)]=l
#        print(p)
#        print()
#        print(l)
        melhores_precisoes = dict()
        
        for K in l:
            self.model = KNeighborsClassifier(p=K)
            self.model.fit(X,y)
            
            particao = RepeatedKFold(n_splits=2, n_repeats=1)
            precisoes = np.mean(cross_val_score(self.model, X, y, cv=particao))
            melhores_precisoes[K]=precisoes
            print("Avaliando classificador com <"+p+">="+str(K)+". Acuraria:", precisoes)

        print("----------")
        key = max(melhores_precisoes, key= lambda k : melhores_precisoes[k])
        
        print("Melhor classficador:"+p+":",key)
        self.model_aux= KNeighborsClassifier(p=key)
        self.model_aux.fit(X,y)
        # Regra do scikit-learn: metodo fit() sempre deve retornar 'self'
        return self

    '''
    predict(T):
    Recebe um conjunto de exemplos de teste e retorna lista com previsoes.
    '''
    def predict(self, T):
        
        # Preencher vetor com a classe mais frequente
        return self.model.predict(T)
#        previsao = []
#        for i in range(len(T)):
#            previsao.append(self.__classe_prevista)
#
#        return previsao

    '''
    score(X,y):
    Recebe exemplos de teste e a classe real dos mesmos. Devolve o percentual
    de exemplos classificados corretamente.
    '''    
    def score(self,x_teste,classe_teste):
        
        # Obter vetor de previsao
        previsao = self.predict(x_teste)
        
        # Retornar percentual de exemplos corretamente classificados
        return metrics.accuracy_score(classe_teste,previsao)

#------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import metrics

# Leitura dos dados
S = datasets.load_breast_cancer()
observacoes = S.data
classe = S.target

m, n = observacoes.shape
print('Numero de exemplos:', m)
print('Numero de caracteristicas:', n)
#splitin dos dados
x_train, x_test, y_train, y_test = train_test_split(
       observacoes, classe , test_size=0.33)
#------------------------------------------------------------------------------
# Construcao do classificador

clf = ClassificadorComAjuste()
clf.fit(x_train,y_train,"n_neighbors",[5,7,9])
y_pred=clf.predict(x_test)

print("Score de acerto prevendo x_test",round(clf.score(x_test,y_test),4))

