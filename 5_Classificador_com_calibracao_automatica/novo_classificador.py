# UFC/DEMA, UFC/MMQ, 2019.1
# Criacao de um classificador para ser usado com recursos do scikit-learn

import numpy as np
from sklearn import datasets, svm
from sklearn.model_selection import RepeatedKFold,\
    RepeatedStratifiedKFold, cross_val_score
from sklearn.base import BaseEstimator

#------------------------------------------------------------------------------
'''
O classificador deve ser derivado de BaseEstimator, deve ter os metodos fit,
predict, e score. O metodo fit deve retornar a referencia self. O classificador
abaixo nao possui hiperparametros e simplesmente detecta a classe mais
frequente no conjunto de treinamento. A classificacao de novos exemplos e' dada
por esta classe.
'''
class Pereba(BaseEstimator):
    '''
    Pereba:
        cp = Pereba()
        Nao ha hiperparametros a configurar.

    '''
    def __init__(self):
        # Atribui um valor padrao para a previsao
        # O valor real deste atributo sera' detectado no metodo 'fit'
        self.__classe_prevista = 0
        pass

    '''
    fit(X, y):
    Detecta e armazena a classe mais frequente no conjunto de treinamento (X,y)
    '''
    def fit(self, X, y):

        # Obter as classes e suas frequencias
        classes, frequencias = np.unique(y, return_counts=True)

        # Armazenar classe mais frequente no conjunto de treinamento
        self.__classe_prevista = classes[np.argmax(frequencias)]

        # Regra do scikit-learn: metodo fit() sempre deve retornar 'self'
        return self

    '''
    predict(T):
    Recebe um conjunto de exemplos de teste e retorna lista com previsoes. As
    previsoes sao todas iguais a self.__classe_prevista.
    '''
    def predict(self, T):
        
        # Preencher vetor com a classe mais frequente
        previsao = []
        for i in range(len(T)):
            previsao.append(self.__classe_prevista)

        return previsao

    '''
    score(X,y):
    Recebe exemplos de teste e a classe real dos mesmos. Devolve o percentual
    de exemplos classificados corretamente.
    '''    
    def score(self, X, y=None):
        
        # Obter vetor de previsao
        previsao = self.predict(X)
        
        # Retornar percentual de exemplos corretamente classificados
        return sum(np.equal(previsao, y))/len(previsao)

#------------------------------------------------------------------------------


# Leitura dos dados
S = datasets.load_breast_cancer()
observacoes = S.data
classe = S.target

m, n = observacoes.shape
print('Numero de exemplos:', m)
print('Numero de caracteristicas:', n)

#------------------------------------------------------------------------------
# Construcao do classificador
per = Pereba()

#------------------------------------------------------------------------------
# Esquema de particao dos dados
particao = RepeatedKFold(n_splits=5, n_repeats=1)

# Precisao da validacao cruzada
precisoes = cross_val_score(per, observacoes, classe, cv=particao)

print('Precisao media:', np.round(np.average(precisoes), 4), end='\n')

#------------------------------------------------------------------------------
