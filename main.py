# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
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
data.reset_index(drop=True, inplace=True) # reseta os indices
#print (data.loc[:, 'sexo':'bairro'])


data = data.drop('time', 1) #excluir coluna
data = data.drop('aceitar', 1) #excluir coluna
#print (data.columns) # teste
#print (data.head(20))


#data = data.replace([5, 4, 3, 2, 1],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
data['fe'] = data['fe'].replace([5, 4, 3, 2, 1],['Muito Alto', 'Alto', 'Médio', 'Baixo', 'Muito Baixo'])
#print (data.fe)


#data = data.replace(['Até R$ 1.100,00 (até 1 s.m.)', 'De R$ 1.100,01 a R$ 3.300,00 (de 1 a 3 s.m.)', 'De R$ 3.300,01 a R$ 5.500,00 (de 3 a 5 s.m.)', 'De R$ 5.500,01 a R$ 11.000,00 (de 5 a 10 s.m.)', 'Mais que R$ 11.000,01 (mais que 10 s.m.)'], ['Até 1 S.M.', 'De 1 a 3 S.M.', 'De 3 a 5 S.M.', 'De 5 a 10 S.M.', 'Mais que 10 S.M.'])
data['renda'] = data['renda'].replace(['Até R$ 1.100,00 (até 1 s.m.)', 'De R$ 1.100,01 a R$ 3.300,00 (de 1 a 3 s.m.)', 'De R$ 3.300,01 a R$ 5.500,00 (de 3 a 5 s.m.)', 'De R$ 5.500,01 a R$ 11.000,00 (de 5 a 10 s.m.)', 'Mais que R$ 11.000,01 (mais que 10 s.m.)'], ['Até 1 S.M.', 'De 1 a 3 S.M.', 'De 3 a 5 S.M.', 'De 5 a 10 S.M.', 'Mais que 10 S.M.'])
#print (data.renda)

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

#data = data.replace(['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'],[5, 4, 3, 2, 1])
#print (data.loc[:, 'apae':'hemocentro'].head(20))

data['pandemia'] = data['pandemia'].replace(['Muito menos', 'Menos', 'Mesma quantidade', 'Mais', 'Muito mais'],['Ajudo muito mais', 'Ajudo mais', 'Ajudo igual', 'Ajudo menos', 'Ajudo muito menos'])
#print (data.pandemia)

# binarização
mlb = MultiLabelBinarizer() #algoritmo de binarização
data['usuario'] = data['usuario'].apply(str).str.replace(', ', ',') #padronizando o formato das virgulas
data["usuario"] = data['usuario'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['usuario'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
#print (expandedLabels)
#data = data.join(expandedLabels) #unindo a tabela principal
data = pd.concat([data, expandedLabels], axis=1)
#print (data[labelClasses])
data = data.drop('usuario', 1) #excluir coluna
data = data.drop('nan', 1) #excluir coluna vazia
#print (data.columns)

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
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro que alguém venha recolher na minha casa', 'Recolher em casa')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Transferência ou Depósito Bancário', 'Transferência ou Depósito')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Correspondência', 'Correspondência')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Pix', 'Pix')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Caixinha de Troco Solidário', 'Troco Solidário')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Rifas e Sorteios', 'Rifas e Sorteios')
data['preferencias'] = data['preferencias'].apply(str).str.replace('Prefiro por Dízimo', 'Dízimo')
data["preferencias"] = data['preferencias'].apply(str).str.split(',')
expandedLabelData = mlb.fit_transform(data['preferencias'])
labelClasses = mlb.classes_
expandedLabels = pd.DataFrame(expandedLabelData, columns=labelClasses) #binarizando coluna
#data = data.join(expandedLabels) #unindo a tabela principal
data = pd.concat([data, expandedLabels], axis=1)
data = data.drop('preferencias', 1) #excluir coluna
#print (data.columns)
#print (data[labelClasses])

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



'''########################### PLOTS ANALISES GERAIS ##########################'''

from plots_gerais import ajuda, bairros, escolaridade, estadoCivil, fe, filhos, genero, idades, meses, midias, ocupacao, pandemia, renda, preferencias, usuario, avaliacao, popularidade, midias2
#bairros(data, 'Distribuição Relativa por Bairros')
#pandemia(data)
#idades(data, 'Distribuição por Idade')
#fe(data, 'Nível de Espiritualidade')
#estadoCivil(data, 'Distribuição por Estado Civil')
#filhos(data, 'Distribuição por Filhos')
#escolaridade(data, 'Distribuição por Escolaridade')
#renda(data, 'Distribuição por Faixa de Renda Domiciliar')
#ocupacao(data, 'Distribuição por Ocupação')
#genero(data, 'Distribuição por Gênero')
#ajuda(data, 'Quem ajuda mais o Terceiro Setor?', 'Quem ajuda menos o Terceiro Setor?')
#midias(data, 'Meios de Comunicação mais Utilizados') # seria melhor com barras?
#meses(data, 'Meses Preferidos para Colaborações') # seria melhor com barras?
#preferencias(data, 'Meios de Colaboração Preferidos')
#usuario(data, 'Proporção de Usuários das Entidades') # seria melhor com barras?


'''########################### PLOTS ANALISES INSTITUIÇÕES ##########################'''

#from avaliacao_plot import avaliacao, popularidade
#avaliacao(data) # ADD ANOTAÇÕES
#popularidade(data) # ADD ANOTAÇÕES

def avaliaBem(data, label):
    bem = data[data[label] != 'Abstenção']
    bem = bem[bem[label] != 'Mediana']
    bem = bem[bem[label] != 'Às vezes é Importante']
    bem = bem[bem[label] != 'Não é Importante']
    return bem

def avaliaRuim(data, label):
    ruim = data[data[label] != 'Abstenção']
    ruim = ruim[ruim[label] != 'Mediana']
    ruim = ruim[ruim[label] != 'Muito Importante']
    ruim = ruim[ruim[label] != 'Importante']
    return ruim

def entidades(data, entidade):
    bem = avaliaBem(data, entidade)
    ruim = avaliaRuim(data, entidade)
    #bairros(bem, 'Bairros daqueles que avaliam BEM a ' + entidade)
    #bairros(ruim, 'Bairros daqueles que avaliam MAL a ' + entidade)
    idades(bem, 'Idades daqueles que avaliam BEM a ' + entidade)
    idades(ruim, 'Idades daqueles que avaliam RUIM a ' + entidade)
    #fe(bem, 'Nível de Espiritualidade daqueles que avaliam BEM a ' + entidade)
    #fe(ruim, 'Nível de Espiritualidade daqueles que avaliam RUIM a ' + entidade)
    #estadoCivil(bem, 'Estado Civil daqueles que avaliam BEM a ' + entidade)
    #estadoCivil(ruim, 'Estado Civil daqueles que avaliam RUIM a ' + entidade)
    #filhos(bem, 'Filhos daqueles que avaliam BEM a ' + entidade)
    #filhos(ruim, 'Filhos daqueles que avaliam RUIM a ' + entidade)
    #escolaridade(bem, 'Escolaridade daqueles que avaliam BEM a ' + entidade)
    #escolaridade(ruim, 'Escolaridade daqueles que avaliam RUIM a ' + entidade)
    #renda(bem, 'Renda Domiciliar daqueles que avaliam BEM a ' + entidade)
    #renda(ruim, 'Renda Domiciliar daqueles que avaliam RUIM a ' + entidade)
    #ocupacao(bem, 'Ocupação daqueles que avaliam BEM a ' + entidade)
    #ocupacao(ruim, 'Ocupação daqueles que avaliam RUIM a ' + entidade)
    #genero(bem, 'Gênero daqueles que avaliam BEM a ' + entidade)
    #genero(ruim, 'Gênero daqueles que avaliam RUIM a ' + entidade)
    #ajuda(bem, 'Quem ajuda mais o Terceiro Setor segundo aqueles que avaliam BEM a ' + entidade, 'Quem ajuda menos o Terceiro Setor segundo aqueles que avaliam BEM a ' + entidade)
    #ajuda(ruim, 'Quem ajuda mais o Terceiro Setor segundo aqueles que avaliam RUIM a ' + entidade, 'Quem ajuda menos o Terceiro Setor segundo aqueles que avaliam RUIM a ' + entidade)
    #midias(bem, 'Meios de Comunicação preferidos por aqueles que avaliam BEM a ' + entidade)
    #midias(ruim, 'Meios de Comunicação preferidos por aqueles que avaliam RUIM a ' + entidade)
    #meses(bem, 'Meses de colaboração preferidos por aqueles que avaliam BEM a ' + entidade)
    #meses(ruim, 'Meses de colaboração preferidos por aqueles que avaliam RUIM a ' + entidade)
    #preferencias(bem, 'Meios de colaboração preferidos por aqueles que avaliam BEM a ' + entidade)
    #preferencias(ruim, 'Meios de colaboração preferidos por aqueles que avaliam RUIM a ' + entidade)
    #usuario(bem, 'Usuários que avaliam BEM a ' + entidade)
    #usuario(ruim, 'Usuários que avaliam RUIM a ' + entidade)

#entidades(data, 'apae')
entidades(data, 'acapam')
#entidades(data, 'aldeiasSOS')
#entidades(data, 'abrigo')
#entidades(data, 'caritas')
#entidades(data, 'fazendaEsperanca')
#entidades(data, 'cvv')
#entidades(data, 'risoterapia')
#entidades(data, 'hemocentro')



'''############################# DOAÇÕES ##################################'''

# DINHEIRO
# TRABALHO VOLUNTÁRIO
# RAÇÃO
# ALIMENTO
# HIGIENE E LIMPEZA
# ROUPAS
# BRINQUEDOS
# SANGUE

# DEFINIR QUEM DOOU MAIS E MENOS



'''################## ALGORITMO APRIORI (REGRA DE ASSOCIAÇÃO) ###################'''

#from apyori import apriori

#data = data.astype(str)
#print (data.head(30))
#print (data.values.tolist())

#association_rules = apriori(data.values.tolist(), min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
#association_results = list(association_rules)
#FONTE: https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/


'''######################## ANALISE DE AGRUPAMENTOS #######################'''

# TRANSFORMAR DADOS EM NUMERICOS
# IDENTIFICAR GRUPOS SEMELHANTES
# CLASSE ALGORITMO CLUSTERING
























