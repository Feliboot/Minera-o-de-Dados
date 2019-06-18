
import numpy as np
import pandas as pd
from sklearn.model_selection import RepeatedKFold,\
    RepeatedStratifiedKFold, cross_val_score
from sklearn.base import BaseEstimator

#------------------------------------------------------------------------------

#função para importar dinamicamente os modulos e as classes
from importlib import import_module
def dynamic_import(abs_module_path, class_name):
    module_object = import_module("sklearn."+abs_module_path)

    target_class = getattr(module_object, class_name)

    return target_class




class ClassificadorSemiSuper(BaseEstimator):
    '''
    ClassificadorComAjuste:
        clf = ClassificadorSemiSuper()
        Classificador que consegue operar metodos de classificação em datasets
        que não possuem todas as classes.
        A partir das observações que possuem classes, é feito o treinamento do
        modelo e esse modelo consegue predizer a classe para as observações que
        não possuem classe.

    '''
    def __init__(self,importar_modelo):
  #     #Pede-se apenas qual o modelo do sklearn que vai ser importado para
#        o classe.
        self.importar_modelo = importar_modelo
        #estou dividindo a string que vem na inicialização da classe, para 
#        passar como parâmetro da função dynamic_import
        self.modulo ,self.classe= self.importar_modelo.split(".")
        
        self.modelo = dynamic_import(self.modulo,self.classe)
        

        pass

    '''
    fit(X, y):
    Detecta e armazena o melhor valor do parametro passado para o modelo.
    '''
    def fit(self, X, y):
#        df = pd.DataFrame(data=X)
#        df["Class"] = y
#        print(df)
        
        
        return self

    '''
    predict(T):
    Recebe um conjunto de exemplos de teste e retorna lista com previsoes.
    '''
    def predict(self, T):
        
        # Preencher vetor com a classe mais frequente
        pass


    '''
    score(X,y):
    Recebe exemplos de teste e a classe real dos mesmos. Devolve o percentual
    de exemplos classificados corretamente.
    '''    
    def score(self,x_teste,classe_teste):
        
        
        pass

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

clf = ClassificadorSemiSuper('neighbors.KNeighborsClassifier')
clf.fit(x_train,y_train)
#y_pred=clf.predict(x_test)

#print("Score de acerto prevendo x_test",round(clf.score(x_test,y_test),4))

