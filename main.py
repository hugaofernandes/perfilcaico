# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas.core import generic
from sklearn.preprocessing import MultiLabelBinarizer


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #remover msg warnings
pd.set_option('display.max_rows', None) # mostrar prints completos

'''######################### ABRINDO A BASE DE DADOS ##############################'''

data = pd.read_csv('./dataset.csv', sep=',') #abrindo o arquivo dataset.csv e separando por virgula
#print (data.columns) # teste 
#print (data) # teste


'''############################ PRE-PROCESSAMENTO DOS DADOS ############################'''

data.columns = ['time', 'sexo', 'idade', 'filhos', 'estadoCivil', 
    'escolaridade', 'ocupacao', 'bairro', 'apae', 'acapam', 'aldeiasSOS', 
    'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro', 
    'usuario', 'ajudaMais', 'ajudaMenos', 'midias', 'dinheiro', 'voluntario', 
    'alimento', 'roupas', 'higiene', 'racao', 'brinquedos', 'sangue', 
    'preferencias', 'meses', 'pandemia', 'fe', 'renda', 'aceitar']

#print (data.columns) # teste
#print (data)


#print (data.idade.head(50))
data = data[data.idade != 'Menor de 18 anos']
#print (data.idade.head(50))

#print (data.bairro.head(50))
data = data[data.bairro != 'Zona Rural']
#print (data.bairro)
data.reset_index(drop=True, inplace=True)
#print (data.loc[:, 'sexo':'bairro'])


data = data.drop('time', 1) #excluir coluna
data = data.drop('aceitar', 1) #excluir coluna
#print (data.columns) # teste
#print (data.head(20))


#data = data.replace([5, 4, 3, 2, 1],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
data['fe'] = data['fe'].replace([5, 4, 3, 2, 1],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
#data = data.replace(['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'],[5, 4, 3, 2, 1])
#print (data.loc[:, 'apae':'hemocentro'].head(20))
#print (data.fe)


#data = data.replace(['Até R$ 1.100,00 (até 1 s.m.)', 'De R$ 1.100,01 a R$ 3.300,00 (de 1 a 3 s.m.)', 'De R$ 3.300,01 a R$ 5.500,00 (de 3 a 5 s.m.)', 'De R$ 5.500,01 a R$ 11.000,00 (de 5 a 10 s.m.)', 'Mais que R$ 11.000,01 (mais que 10 s.m.)'], ['Até 1 S.M.', 'De 1 a 3 S.M.', 'De 3 a 5 S.M.', 'De 5 a 10 S.M.', 'Mais que 10 S.M.'])
data['renda'] = data['renda'].replace(['Até R$ 1.100,00 (até 1 s.m.)', 'De R$ 1.100,01 a R$ 3.300,00 (de 1 a 3 s.m.)', 'De R$ 3.300,01 a R$ 5.500,00 (de 3 a 5 s.m.)', 'De R$ 5.500,01 a R$ 11.000,00 (de 5 a 10 s.m.)', 'Mais que R$ 11.000,01 (mais que 10 s.m.)'], ['Até 1 S.M.', 'De 1 a 3 S.M.', 'De 3 a 5 S.M.', 'De 5 a 10 S.M.', 'Mais que 10 S.M.'])
#print (data.renda)

# binarização
mlb = MultiLabelBinarizer() #algoritmo de binarização
data['usuario'] = data['usuario'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["usuario"] = data['usuario'].apply(str).str.split(',')
#print (data['usuario'])
expandedLabelData = mlb.fit_transform(data['usuario'])
labelClasses = mlb.classes_
#print (labelClasses)
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
#print (expandedLabels)
#data = data.join(expandedLabels) #unindo a tabela principal
data = pd.concat([data, expandedLabels], axis=1)
#print (data[labelClasses])
data = data.drop('usuario', 1) #excluir coluna
data = data.drop('nan', 1) #excluir coluna vazia
#print (data[labelClasses])
#print (data.columns)
#print (data.loc[:, 'APAE Caicó':].head(20))

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['midias'] = data['midias'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["midias"] = data['midias'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['midias'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = pd.concat([data, expandedLabels], axis=1)
#data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('midias', 1) #excluir coluna
#print (data.columns)
#print (data[labelClasses])

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['preferencias'] = data['preferencias'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["preferencias"] = data['preferencias'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['preferencias'])
#print (expandedLabelData)
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
#data = data.join(expandedLabels) #unindo a tabela principal
data = pd.concat([data, expandedLabels], axis=1)
data = data.drop('preferencias', 1) #excluir coluna
#print (data.columns)
#print (expandedLabels)
#print (data[labelClasses])
data = data.rename(columns={'Prefiro que alguém venha recolher na minha casa' : 'Recolher em casa',
                            'Prefiro por Transferência ou Depósito Bancário' : 'Transferência ou Depósito',
                            'Prefiro por Correspondência' : 'Correspondência',
                            'Prefiro por Pix' : 'Pix',
                            'Prefiro por Caixinha de Troco Solidário' : 'Troco Solidário',
                            'Prefiro por Rifas e Sorteios' : 'Rifas e Sorteios',
                            'Prefiro por Dízimo' : 'Dízimo'})
#print (data.columns)

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['meses'] = data['meses'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["meses"] = data['meses'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['meses'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = pd.concat([data, expandedLabels], axis=1)
#data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('meses', 1) #excluir coluna
#print (data.columns)
#print (data[labelClasses])


#data = data.replace(np.nan, 'Abstenção')
data['apae'] = data['apae'].replace(np.nan, 'Abstenção')
data['acapam'] = data['acapam'].replace(np.nan, 'Abstenção')
data['aldeiasSOS'] = data['aldeiasSOS'].replace(np.nan, 'Abstenção')
data['abrigo'] = data['abrigo'].replace(np.nan, 'Abstenção')
data['caritas'] = data['caritas'].replace(np.nan, 'Abstenção')
data['fazendaEsperanca'] = data['fazendaEsperanca'].replace(np.nan, 'Abstenção')
data['cvv'] = data['cvv'].replace(np.nan, 'Abstenção')
data['risoterapia'] = data['risoterapia'].replace(np.nan, 'Abstenção')
data['hemocentro'] = data['hemocentro'].replace(np.nan, 'Abstenção')
#print (data.loc[:, 'apae':'hemocentro'])




'''########################### PLOTS ANALISES GERAIS ##########################'''


from bairros_plot import bairros
#bairros(data) # PRECISA DE AJUSTES

from pandemia_plot import pandemia
#pandemia(data) # PRECISA DE AJUSTES

from idades_plot import idades
#idades(data)

from fe_plot import fe
#fe(data)

from estadoCivil_plot import estadoCivil
#estadoCivil(data)

from filhos_plot import filhos
#filhos(data)

from escolaridade_plot import escolaridade
#escolaridade(data)

from renda_plot import renda
#renda(data)

from ocupacao_plot import ocupacao
#ocupacao(data)

from genero_plot import genero
#genero(data)

from ajuda_plot import ajuda
#ajuda(data)

from midias_plot import midias
#midias(data)

from meses_plot import meses
#meses(data)

from preferencias_plot import preferencias
#preferencias(data)

from avaliacao_plot import avaliacao
#avaliacao(data) # PRECISA DE AJUSTES














'''################################# ANALISES DESCRITIVAS #########################################
(Q1) É possível traçar um perfil de quem está disposto a colaborar, de qualquer forma, 
com instituições beneficentes no município de Caicó/RN? É possível identificar o 
padrão de renda dessas pessoas, os setores da cidade onde residem, sua escolaridade, 
gênero, faixa etária, como costumam ou preferem ajudar, quais instituições conhecem e 
como as avaliam, dentre outras informações?

(Q2) Os resultados da análise dos dados coletados ajuda na tomada de decisão do
 trabalho desenvolvido pelas ONGs da Cidade de Caicó/RN? Esses dados podem ajudar na 
 captação de recursos para essas entidades?

(Q3) Os dados coletados podem descrever um panorama ou retrato do Terceiro Setor 
no Município de Caicó/RN?
'''






'''################## ALGORITMO APRIORI (REGRA DE ASSOCIAÇÃO) ###################'''

#from apyori import apriori

#data = data.astype(str)
#print (data.head(30))
#print (data.values.tolist())

#association_rules = apriori(data.values.tolist(), min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
#association_results = list(association_rules)
#FONTE: https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/



'''

################### POR INSTITUIÇÃO ###################
apae, acapam, abrigo pedro gurgel, aldeias SOS, caritas, 
fazenda da esperança, CVV, risoterapia, hemocentro


    GRÁFICO 4X4
        AVALIAÇÃO
        MEIOS DE COMUNICAÇÃO
        BAIRROS
        PREFERÊNCIAS

    Descrever POPULARIDADE
    Descrever se JÁ PRECISOU DOS SERVIÇOS
    Descrever a IDADE, GÊNERO, ESTADO CIVIL e FILHOS
    Descrever os PREFERÊNCIAS e MESES
    Descrever OCUPAÇÃO, RENDA e ESCOLARIDADE
    Descrever o EFEITO DA PANDEMIA



################# DOAÇÕES ##################

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        GERAL, quem doou algo

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        DINHEIRO

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        RAÇÃO

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        ALIMENTO

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        ROUPAS

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        TRABALHO VOLUNTÁRIO

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        HIGIENE E LIMPEZA

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        BRINQUEDOS

    2x2 - GRÁFICO PIZZA (relativo) e HISTOGRAMA (absoluto)
        SANGUE

    DEFINIR QUEM DOA MAIS E QUEM DOA MENOS
        E QUAIS SUAS PRINCIPAIS CARACTERÍSTICAS


################ ANALISES INFERENCIAIS #################

    AGRUPAMENTO
    ASSOCIAÇÃO

'''

