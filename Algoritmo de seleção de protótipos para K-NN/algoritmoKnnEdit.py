import numpy as np
import pandas as pd
import matplotlib as plt

def distanciaEuclidiana(a, b):
    d = (a[0] - b[0])**2 + (a[1] - b[1])**2
    return np.sqrt(d)

#------------------------------------------------------------------------------
# Dimensoes dos dados
m =  500   # Numero de exemplos na amostra
t =  100   # Numero de exemplos de teste

# Numero de vizinhos
K = 3

# Numero de classes
C = 2 # Assumimos neste codigo que as classes dos dados sao: 0, 1, ..., C-1

#------------------------------------------------------------------------------
# Gerar exemplos de treinamento aleatoriamente
# np.random.seed(8)                    # Semente do gerador aleatorio
S = np.random.rand(m,2)                # Exemplos da amostra

# Informacao de classe
# Neste codigo, a classe de um exemplo de treinamento e' 1 se a distancia
# do exemplo ate o ponto (0.5,0.5) e' maior que 0.3; caso contrario, a
# classe do exemplo e' 0.
classe_S = [1]*m
for i in range(m):
    d = distanciaEuclidiana(S[i], [0.5, 0.5])
    if d < 0.3:
        classe_S[i] = 0

df = pd.DataFrame(data = S, columns = ["x1","x2"])
df["Classe"] = classe_S