# Introducao aa Mineracao de Dados, 2019.1, UFC/DEMA
#
# Gerar todos os monomios de grau 1, 2, e 3
# Cada monomio sera' representado por um tupla

n = 4 # Numero total de variables: x1, x2, ..., xn

# Conjunto de literais
literais = []
for i  in range(1,n+1):
    literais.append(i)
    literais.append(-i)

print('Literais:', literais)


# Monomios de grau 1
M1 = []
for u in literais:
    M1.append((u,))
    
print('\nMonomios de grau 1:')
print('M1 = ', M1, end='\n\n')


# Monomios de grau 2
M2 = []
for mon in M1:
    for u in literais:
        if abs(u) > abs(mon[-1]):
            M2.append(mon + (u,))

print('Monomios de grau 2:')
print('M2 = ', M2, end='\n\n')


# Monomios de grau 3
M3 = []
for mon in M2:
    for u in literais:
        if abs(u) > abs(mon[-1]):
            M3.append(mon + (u,))

print('Monomios de grau 3:')
print('M3 = ', M3, end='\n\n')

# Monomios de grau 1, 2 e 3 juntos
M = M1 + M2 + M3

print('Monomios de grau 1, 2, e 3:')
print('M = ', M)

#------------------------------------------------------------------------------
# Versao alternativa
# Aqui, cada monomio e' representado por uma lista de n valores em {0,1,-1}:
# 0 significa ausencia, 1 literal positivo, -1 literal negado

import itertools as it

# Gera todos os monomios, inclusive de grau 0 e de grau maior que 3
A = [0, 1, -1]
Todos = itertools.product(A, repeat=n)
Todos = [list(i) for i in Todos]

# Guardar em M apenas os monomios de grau 1, 2, e 3
M = []
for monomio in Todos:
    c = [abs(v) for v in monomio]
    if 1 <= sum(c) <= 3:
        M.append(monomio)

print('\n----------------------------------------------------------------\n')
print('Monomios de grau 1, 2, e 3:')
print(M)
