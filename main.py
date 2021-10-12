# -*- coding: utf-8 -*-

#from plotsDescritivos import idades, comunicacao
#from tratamento import colunasNome, testeColunasNome, excluirColuna, testeExcluirColuna, notasToInt, testeNotasToInt, binarizacao, testeBinarizacao, testeToTexto, toTexto
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #remover msg warnings
pd.set_option('display.max_rows', None) # mostrar prints completos


data = pd.read_csv('./dataset.csv', sep=',') #abrindo o arquivo dataset.csv e separando por virgula
#print (data.columns) # teste 
#print (data.head(10)) # teste


############################ TRATAMENTO DOS DADOS ############################

data.columns = ['time', 'sexo', 'idade', 'filhos', 'estadoCivil', 
    'escolaridade', 'ocupacao', 'bairro', 'apae', 'acapam', 'aldeiasSOS', 
    'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro', 
    'usuario', 'ajudaMais', 'ajudaMenos', 'midias', 'dinheiro', 'voluntario', 
    'alimento', 'roupas', 'higiene', 'racao', 'brinquedos', 'sangue', 
    'preferencias', 'meses', 'pandemia', 'fe', 'renda', 'aceitar']

#print (data.columns) # teste
#print (data.head(10))


#print (data.idade.head(50))
data = data[data.idade != 'Menor de 18 anos']
#print (data.idade.head(50))

#print (data.bairro.head(50))
data = data[data.bairro != 'Zona Rural']
#print (data.bairro.head(50))


data = data.drop('time', 1) #excluir coluna
data = data.drop('aceitar', 1) #excluir coluna
#print (data.columns) # teste
#print (data.head(20))


# binarização
mlb = MultiLabelBinarizer() #algoritmo de binarização
data['usuario'] = data['usuario'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["usuario"] = data['usuario'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['usuario'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('usuario', 1) #excluir coluna
data = data.drop('nan', 1) #excluir coluna vazia
#print (data.columns)
#print (data.loc[:, 'APAE Caicó':].head(20))

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['midias'] = data['midias'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["midias"] = data['midias'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['midias'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('midias', 1) #excluir coluna
#print (data.columns)
#print (data.loc[:, 'Blogs e Sites':].head(20))

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['preferencias'] = data['preferencias'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["preferencias"] = data['preferencias'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['preferencias'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('preferencias', 1) #excluir coluna
#print (data.columns)
#print (data.loc[:, 'Prefiro por Caixinha de Troco Solidário':].head(20))

mlb = MultiLabelBinarizer() #algoritmo de binarização
data['meses'] = data['meses'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["meses"] = data['meses'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['meses'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
data = data.join(expandedLabels) #unindo a tabela principal
data = data.drop('meses', 1) #excluir coluna
#print (data.columns)
#print (data.loc[:, 'Abril':].head(20))


data = data.replace(np.nan, 0)
#print (data.loc[:, 'apae':'hemocentro'].head(20))

#data = data.replace(['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'],[5, 4, 3, 2, 1])





'''

#testeColunasNome(data)
data = colunasNome(data)

#testeExcluirColuna(data, 'time')
data = excluirColuna(data, 'time')
#testeExcluirColuna(data, 'aceitar')
data = excluirColuna(data, 'aceitar')

#testeNotasToInt(data, 30)
data = notasToInt(data)

#testeBinarizacao(data, 'midias', 30)
data, midias = binarizacao(data, 'midias')
#testeBinarizacao(data, 'preferencias', 30)
data, preferencias = binarizacao(data, 'preferencias')
#testeBinarizacao(data, 'meses', 100)
data, meses = binarizacao(data, 'meses')

#testeToTexto(data, 20)
#data = toTexto(data)


#idades(data, 'idade')
comunicacao(data, midias)

'''



'''
##################### ANALISES DESCRITIVAS ######################

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


############# ANALISES GERAIS ###############

    HISTOGRAMA 2x2 (absolutos e relativos)
        BAIRROS

    HISTOGRAMA (absolutos e relativos)
        EFEITO DA PANDEMIA

    GRÁFICO PIZZA 4x4
        IDADE
        ESPIRITUALIDADE
        ESTADO CIVIL
        FILHOS

    GRÁFICO PIZZA 4x4
        ESCOLARIDADE
        RENDA
        OCUPAÇÃO
        GÊNERO

    GRÁFICO PIZZA 2x2
        FINANCIA MAIS
        FINANCIA MENOS

    GRÁFICO PIZZA 4x4
        MEIO DE COMUNICAÇÃO
        PREFERÊNCIAS
        MESES
        AVALIAÇÃO



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


################ ANALISES INFERENCIAIS #################

    AGRUPAMENTO
    ASSOCIAÇÃO

'''

