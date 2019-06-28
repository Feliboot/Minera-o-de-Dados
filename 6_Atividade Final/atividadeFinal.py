#Felipe Araujo
#Lucas Noleto
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
    def __init__(self,importar_modelo,k):
        #inicialização do classificadorSemiSuper, onde se passa por parâmetro
        #qual modelo a ser importado e qual valor de K_exemplos desejados
        #por iteração da predição
        self.importar_modelo = importar_modelo
        #estou dividindo a string que vem na inicialização da classe, para 
#        passar como parâmetro da função dynamic_import
        self.modulo ,self.classe= self.importar_modelo.split(".")
        self.modelo = dynamic_import(self.modulo,self.classe)
        self.k = k

        pass

    '''
    fit(X, y):
    Detecta qual observação não possui classe (classe = -1) e treina o modelo
    com as observações que tem classe, posteriormente prediz as observações que
    sem classes, faz uma junção dessas observações com a classe predita com a 
    observações usadas em treino.
    '''
    def fit(self, X, y):
#        inicializando o classificador
        self.clf = self.modelo()
        #variaveis auxiliares
        #variaveis com deselegantes significa que sao variaveis ligadas
        #a observações sem classe, piada ruim né? Sabemos, ainda bem
        #que escolhemos não viver de stand up kkkk
        indice_deselegantes = []
        #por sua vez.as variaveis elegantes são as que possui classe
        indice_elegantes=[]
        y_dataFrameElegante=[]
        #Variavel auxiliar
        i=0
        for classe in y:
            if classe ==-1:
               indice_deselegantes.append(i)
            else:
                indice_elegantes.append(i)
                y_dataFrameElegante.append(classe)
            i=i+1
        
        #dataframe que será utilizado para predição
        x_dataFrameDeselegante = X.iloc[indice_deselegantes]
        #dataframe que será utilizado para treino
        x_dataFrameElegante = X.iloc[indice_elegantes]
        #quantidade de iterações para realizar
        qtd_iteracoes = len(x_dataFrameDeselegante)/self.k
        #resto da divisão, k pode ser um numero não multiplo do tamanho do 
        #dataset
        resto = len(x_dataFrameDeselegante) % self.k
        #valor total das amostras
        valor_total = len(x_dataFrameElegante) + len(x_dataFrameDeselegante)
        
        #valores auxiliares.
        #comeco = inicio do slice das observações
        comeco = 0
        #fim do slice das observações
        fim = self.k
        #contador de quantas observações ja foram treinadas.
        contador=0
        #criando um dataFrame S de auxilio.
        S=pd.DataFrame()
        
        self.clf.fit(x_dataFrameElegante,y_dataFrameElegante)
        #print a baixo para ver a quantidade de linhas das observações de 
        #treino.
        #print(len(x_dataFrameElegante))
        for j in range(int(qtd_iteracoes)):
            
            if((((len(x_dataFrameDeselegante))-contador) > int(self.k))):    
                S = pd.concat([S,x_dataFrameElegante.iloc[comeco:fim]])
                comeco = fim
                fim = fim+self.k
                y_pred = self.clf.predict(S)
                x_dataFrameElegante= pd.concat([x_dataFrameElegante,S])
                y_dataFrameElegante=y_pred
                contador=contador+self.k                  
            
            S=pd.DataFrame()
        
        if (resto>0):
            S=pd.DataFrame()
            S = pd.concat([S,x_dataFrameElegante.iloc[comeco:comeco+resto]])
            y_pred = self.clf.predict(S)
            x_dataFrameElegante= pd.concat([x_dataFrameElegante,S])
            y_dataFrameElegante=y_pred
        
        else:
            S=pd.DataFrame()
            S = pd.concat([S,x_dataFrameElegante.iloc[comeco:comeco+(abs(len(x_dataFrameDeselegante))-contador)]])
            y_pred = self.clf.predict(S)
            x_dataFrameElegante= pd.concat([x_dataFrameElegante,S])
            y_dataFrameElegante=y_pred
        
        
        #Codigo abaixo apenas para verificação se todas as amostras estão no 
        #dataframe de treino
        if(valor_total == len(x_dataFrameElegante)):
            print("Tudo está elegante agora!")

        return self

    '''
    predict(T):
    Recebe um conjunto de exemplos de teste e retorna a predição dessas
    observações.
    '''
    def predict(self, T):
        
        #utiliza o metodo  predict do classificador escolhido.
        return self.clf.predict(T)
        

    '''
    score(X,y):
    Recebe exemplos de teste e a classe real dos mesmos. Devolve o percentual
    de exemplos classificados corretamente.
    '''    
    def score(self,classe_teste,y_predito,):
#        utilizando o metric.accuracy_score para analisar os valores de acerto.
        
        return metrics.accuracy_score(classe_teste,y_predito)


#------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import time

#variavel que auxiliará para medição do tempo de execução do algoritmo
inicio = time.time()


#------------------------------------------------------------------------------


df = pd.read_csv("heart.csv")

#print(df)
m,n = df.shape
#print(df.shape)
#dividindo o DataSet em observações e classes
observacoes = df.iloc[:,0:n-1]
classe = df.iloc[:,-1]


#Os valores escolhidos de K escolhidos foram baixos por questões do 
#tamanho do conjunto de dados
melhores_precisoes = dict()
lista_K = [1,2,3,4,5,6,7,8,9,10]



for K_values in lista_K:
    x_train, x_test, y_train, y_test = train_test_split(
           observacoes, classe , test_size=0.33)
    
    x_A, x_B, y_A, y_B = train_test_split(
           x_train, y_train , test_size=0.5)
    
    df_comClasses= pd.DataFrame(columns = df.columns, data = x_A)
    df_comClasses['Class'] = y_A
    
    df_semClasses= pd.DataFrame(columns = df.columns, data = x_B)
    df_semClasses['Class'] = -1
    
    df_Treino = pd.DataFrame()
    df_Treino = pd.concat([df_comClasses, df_semClasses])
    
    model = ClassificadorSemiSuper("ensemble.AdaBoostClassifier",K_values)
    model.fit(df_Treino.iloc[:,0:n-1],df_Treino.iloc[:,-1])
    saida_predita = model.predict(x_test)
    
    precisoes = (model.score(y_test,saida_predita))
    melhores_precisoes[K_values]=precisoes
    print("Avaliando classificador com valor de K:"+str(K_values)+". Acuraria:", round(precisoes,4))
    
    
#variavel que receberá o K com maior acuraria
key = max(melhores_precisoes, key= lambda k : melhores_precisoes[k])       
print("Melhor Valor de k:",key)
print()
fim = time.time()
print("Tempo de execução do cod em minutos:",(fim - inicio)/60)





