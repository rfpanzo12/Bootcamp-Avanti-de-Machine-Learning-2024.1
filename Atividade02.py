######################################## Questão 1 ########################################
def lista_impar(lista):
    _lista = []
    for i in lista:
        if i%2 != 0:
            _lista.append(i)
    
    return _lista


    
######################################## Questão 2 ########################################
def lista_primo(lista):
    _lista = []
    for i in lista:
        div = 0
        for j in range(1, i+1):
            if i%j == 0:
                div = div + 1;
        if div == 2:    
            _lista.append(i)
    
    return _lista


    
######################################## Questão 3 ########################################
def lista_diferentes(lista1, lista2):
    _lista = []
    for i in lista1:
        if i not in lista2:    
            _lista.append(i)
            
    for i in lista2:
        if i not in lista1:    
            _lista.append(i)
    
    return _lista

    
  
######################################## Questão 4 ########################################
def segundo_maior(lista):
    _lista = lista
    try:
        maior = max(_lista)
        _lista.remove(maior)
        return max(_lista)
    except:
        return "A lista tem apenas um elmento!\n"

      

######################################## Questão 5 ########################################
def lista_nomes(lista):
    _lista = []
    for i in lista:
        _lista.append(i[0])
    _lista.sort()
    
    return _lista
    
    
    
######################################## Questão 6 ########################################
'''
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                              transform=axs[row, col].transAxes,
                              ha='center', va='center', fontsize=18,
                              color='darkgrey')

fig.suptitle('plt.subplots()')
'''



######################################## Questão 7 ########################################
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
'''



######################################## Questão 8 ########################################
'''
import pandas as pd #Importa a biblioteca Pandas

df = pd.read_csv('nome_do_arquivo.csv') #Carrega o arquivo
print(df.head()) #Imprime as primeiras linhas
'''



######################################## Questão 9 ########################################
'''Para selecionar uma coluna específica em um DataFrame do pandas, usa-se a notação de colchetes [] 
ou a notação de ponto. Para filtrar linhas com base em uma condição, usa-se a função loc[] ou iloc[].

Ex:

import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({
    'nome': ['Rufino', 'Sergío', 'Panzo],
    'idade': [20, 25, 30],
})

# Selecionar uma coluna específica
col_idade = df['idade']
# Ou 
col_idade = df.idade

# Filtrar linhas com base em uma condição
condicao = df['idade'] > 21
lin_filtradas = df.loc[condicao]

# Exibir o resultado
print("Coluna 'idade':")
print(col_idade)
print("\nLinhas filtradas:")
print(lin_filtradas)
'''



######################################## Questão 10 ########################################
'''Para lidar com valores ausentes (NaN) em um DataFrame do pandas, podemos usar técnicas, como 
a remoção das linhas ou colunas que contêm valores ausentes ou ainda, o preenchendo os valores 
ausentes com um valor específico ou não.

Ex:
    # Remoção de linhas
    df.dropna(inplace=True)
    # Remoção de colunas
    df.dropna(axis=1, inplace=True)
    
    # Preenchimento de valores ausentes com o valor específico 0
    df.fillna(0, inplace=True)
'''







