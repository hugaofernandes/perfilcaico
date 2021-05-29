
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from matplotlib import colors
#from matplotlib.ticker import PercentFormatter
#from apyori import apriori
from sklearn.preprocessing import MultiLabelBinarizer


def colunasNome(data):
    data.columns = ['time', 'sexo', 'idade', 'filhos', 'relacionamento', 
    'bairro', 'apae', 'acapam', 'aldeias', 'abrigo', 'casaCaridade', 
    'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 
    'hemocentro', 'precisou', 'ajudaMais', 'ajudaMenos', 'midias', 
    'dizimo', 'dinheiro', 'voluntario', 'alimento', 'roupas', 'higiene', 
    'racao', 'brinquedos', 'sangue', 'preferencias', 'meses', 'pandemia', 
    'fe', 'ocupacao', 'escolaridade', 'renda', 'aceitar']
    return data

def testeColunasNome(data):
    print ('COLUNAS(ANTES):\n', data.columns) # teste
    print()
    print ('COLUNAS(DEPOIS):\n', colunasNome(data).columns) # teste

def excluirColuna(data, coluna):
    data = data.drop(coluna, 1) #excluir coluna
    return data

def testeExcluirColuna(data, coluna):
    print ('COLUNAS(ANTES):\n', data.columns) # teste
    print()
    print ('COLUNAS(DEPOIS):\n', excluirColuna(data, coluna).columns) # teste

def notasToInt(data):
    data = data.replace(['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5'],[1, 2, 3, 4, 5])
    data = data.replace(np.nan, 0)
    return data

def testeNotasToInt(data, nlinhas):
    print ('NOTAS(ANTES):\n', 
    data.loc[:, 'apae':'hemocentro'].head(nlinhas)) # teste
    print()
    print ('NOTAS(DEPOIS):\n', 
    notasToInt(data).loc[:, 'apae':'hemocentro'].head(nlinhas)) # teste

def binarizacao(data, coluna):
    mlb = MultiLabelBinarizer() #algoritmo de binarização
    data[coluna] = data[coluna].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
    data[coluna] = data[coluna].apply(str).str.split(',')
    expandedLabelData = mlb.fit_transform(data[coluna])
    labelClasses = mlb.classes_
    expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
    data = data.join(expandedLabels) #unindo a tabela principal
    data = excluirColuna(data, coluna) #excluindo coluna
    return data, labelClasses # labelsClasses é retornado apenas para fins de testes

def testeBinarizacao(data, coluna, nlinhas):
    print ('COLUNA '+ coluna +'(ANTES):\n', data[coluna].head(nlinhas)) # teste
    print()
    new_data, labels = binarizacao(data, coluna)
    print ('COLUNA BINARIZADA '+ coluna +'(DEPOIS):\n', 
    new_data.loc[:, labels].head(nlinhas)) # teste

def toTexto(data):
    return data.astype(str)

def testeToTexto(data, nlinhas):
    print ('DADOS(ANTES):\n', data.head(nlinhas)) # teste
    print()
    print ('DADOS(DEPOIS):\n', toTexto(data).head(nlinhas)) # teste


