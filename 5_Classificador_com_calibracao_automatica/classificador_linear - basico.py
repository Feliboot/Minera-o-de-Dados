import numpy as np
from sklearn import neighbors, datasets
from sklearn.base import BaseEstimator
from sklearn.model_selection import StratifiedKFold, cross_val_score
import matplotlib as plt


class ClassificadorLinear(BaseEstimator):

    # Construtor do classificador -- define valores 'default' dos parametros
    def __init__(self, eta=0.15, max_iteracoes=1000):
        self._eta = eta
        self._max_iteracoes = max_iteracoes
    

    # Fase de treinamento    
    def fit(self, X, y):
        if len(np.unique(y)) != 2:
            raise ValueError('Numero de classes invalido (deve ser 2).')
            return None
        else:
            n_exemplos, n_carac = X.shape
            self._n_caracteristicas = n_carac

            # Aqui acontece o treinamento do classificador

            # Plotar dados de treinamento
            for i in range(n_exemplos):
                if y[i] == 1:
                    plt.pyplot.scatter(x=[X[i][0]], y=[X[i][1]],
                                       c=[[0,0,1]], marker='s')
                else:
                    plt.pyplot.scatter(x=[X[i][0]], y=[X[i][1]],
                                       c=[[1,0,0]], marker='s')
            plt.pyplot.gca().set_facecolor((1., 1., 1.))
            plt.pyplot.show()

            return self


    # Fase de teste
    def predict(self, T):
        m, n = np.array(T).shape
        if n != self._n_caracteristicas:
            raise ValueError('Teste incompativel com conjunto de treinamento.')
            return None
        else:
            
            # Aqui acontece a classificacao dos exemplos de teste
            
            previsao = [1]*len(T)
            return previsao


    # E' chamado pelos objetos KFold, StratifiedKFold, e similares    
    def score(self, X, y=None):
        previsao = self.predict(X)

        # Plotar dados de teste
        m, n = np.array(X).shape
        for i in range(m):
            if y[i] == 1:
                plt.pyplot.scatter(x=[X[i][0]], y=[X[i][1]],
                                   c=[[0,0,1]], marker='x')
            else:
                plt.pyplot.scatter(x=[X[i][0]], y=[X[i][1]],
                                   c=[[1,0,0]], marker='x')
        plt.pyplot.gca().set_facecolor((.9, .9, .9))
        plt.pyplot.show()

        # Retornar percentual de acertos
        return sum(np.equal(previsao, y))/len(previsao)



#------------------------------------------------------------------------------
# Leitura dos dados do dataset Iris
# Vamos usar apenas duas caracteristicas (a primeira e a ultimaa) e
# vamos considerar as classes 1 e 2 como uma so classe (de etiqueta 1)

iris = datasets.load_iris()
X_iris = iris.data[...,[0,3]]
y_iris = iris.target

for i in range(m):
    if y_iris[i] == 2:
        y_iris[i] = 1

[m,n] = iris.data.shape
print('Numero de exemplos:', m)
print('Numero de caraceristicas:', n, end='\n\n')


#------------------------------------------------------------------------------
# Validacao cruzada com nosso classificador

particao = StratifiedKFold(n_splits=3, shuffle=True)

lin = ClassificadorLinear() # Testar substituir 'lin' por KNeighborsClassifier

precisoes = []

for treinamento, teste in particao.split(X_iris, y_iris):

    print('Classes dos exemplos de teste:', y_iris[teste])
    lin.fit(X_iris[treinamento], y_iris[treinamento])
    precisao = lin.score(X_iris[teste], y_iris[teste])
    precisoes.append(precisao)

print('Precisoes:', precisoes)
print('Precisao media:', np.average(precisoes))

#------------------------------------------------------------------------------
