# -*- coding: utf-8 -*-

#from plotsDescritivos import idades, comunicacao
#from tratamento import colunasNome, testeColunasNome, excluirColuna, testeExcluirColuna, notasToInt, testeNotasToInt, binarizacao, testeBinarizacao, testeToTexto, toTexto
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from apyori import apriori
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #remover msg warnings
pd.set_option('display.max_rows', None) # mostrar prints completos



data = pd.read_csv('./dataset.csv', sep=',') #abrindo o arquivo dataset.csv e separando por virgula
#print (data.columns) # teste 
#print (data.head(10)) # teste


'''############################ TRATAMENTO DOS DADOS ############################'''

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


data = data.replace(np.nan, 'Abstenção')
#print (data.loc[:, 'apae':'hemocentro'].head(20))

data = data.replace([5, 4, 3, 2, 1],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
#data = data.replace(['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'],[5, 4, 3, 2, 1])
#data = data.fe.replace(['5', '4', '3', '2', '1'],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
#data['fe'] = data['fe'].apply(str).str.replace(['5', '4', '3', '2', '1'],['Máximo', 'Alto', 'Médio', 'Baixo', 'Mínimo'])
#print (data.loc[:, 'apae':'hemocentro'].head(20))
#print (data.fe.head(20))

#data['renda'] = data['renda'].apply(str).str.replace([' (até 1 s.m.)', ' (a 1 a 3 s.m.)', ' (de 3 a 5 s.m.)', ' (de 5 a 10 s.m.)', ' (mais que 10 s.m.)'],[''])
#data['renda'] = data['renda'].apply(str).str.replace(' (até 1 s.m.)','')
data = data.replace(['Até R$ 1.100,00 (até 1 s.m.)', 'De R$ 1.100,01 a R$ 3.300,00 (de 1 a 3 s.m.)', 'De R$ 3.300,01 a R$ 5.500,00 (de 3 a 5 s.m.)', 'De R$ 5.500,01 a R$ 11.000,00 (de 5 a 10 s.m.)', 'Mais que R$ 11.000,01 (mais que 10 s.m.)'], 
['Até 1 S.M.', 'De 1 a 3 S.M.', 'De 3 a 5 S.M.', 'De 5 a 10 S.M.', 'Mais que 10 S.M.'])





'''################################# ANALISES DESCRITIVAS ##########################3###############'''

#############################################################################
# histograma 2x2 = BAIRROS
fig, axs = plt.subplots(2, 1, tight_layout=True)
axs[0].hist(data['bairro'], bins=len(data['bairro']))
axs[0].set_title('Distribuição por Bairros Absolutas')
#plt.xticks(rotation=50, wrap=True)
plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=60, wrap=True)
axs[1].hist(data['bairro'], bins=len(data['bairro']), density=True)
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
axs[1].set_title('Distribuição por Bairros Relativas')
#plt.xticks(rotation=50, wrap=True)
plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=60, wrap=True)
plt.show()


'''
#############################################################################
# grafico pizza 4x4 = IDADE, ESPIRITUALIDADE, ESTADO CIVIL e FILHOS
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) 

# proporção por idade
#fig, ax1 = plt.subplots()
labels = data.idade.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.idade == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0.5), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Distribuição por Idade')
#plt.show()

# proporção de espiritualidade
#fig, ax2 = plt.subplots()
labels = data.fe.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.fe == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Nível de Espiritualidade')
#plt.show()

# proporção por estado civil
#fig, ax3 = plt.subplots()
labels = data.estadoCivil.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.estadoCivil == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax3.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
ax3.set_title('Distribuição por Estado Civil')
#plt.show()

# proporção de filhos
#fig, ax4 = plt.subplots()
labels = data.filhos.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.filhos == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax4.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
ax4.set_title('Distribuição por Filhos')
plt.show()
'''

'''
###############################################################################################################
# grafico pizza 4x4 = ESCOLARIDADE, RENDA, OCUPAÇÃO e GÊNERO
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) 

# proporção por ESCOLARIDADE
#fig, ax1 = plt.subplots()
labels = data.escolaridade.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.escolaridade == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0.5), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Distribuição por Escolaridade')
#plt.show()

# proporção de Renda
#fig, ax2 = plt.subplots()
labels = data.renda.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.renda == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Distribuição por Renda')
#plt.show()

# proporção por ocupação
#fig, ax3 = plt.subplots()
labels = data.ocupacao.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.ocupacao == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax3.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
ax3.set_title('Distribuição por Ocupação')
#plt.show()

# proporção de genero
#fig, ax4 = plt.subplots()
labels = data.sexo.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.sexo == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax4.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax4.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
ax4.set_title('Distribuição por Gênero')
plt.show()
'''

'''
############################################################################
# grafico pizza 2x2 = AJUDA MAIS e AJUDA MENOS
fig, (ax1, ax2) = plt.subplots(1, 2)

#fig, ax1 = plt.subplots()
labels = data.ajudaMais.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.ajudaMais == i]))
explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
pie = ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.legend(pie[0],labels, bbox_to_anchor=(0,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
#ax1.legend(labels, loc='lower left')
ax1.set_title('Quem ajuda mais o Terceiro Setor?')
#plt.show()

#fig, ax2 = plt.subplots()
#labels = data.ajudaMenos.unique().tolist()
sizes = []
for i in labels:
    sizes.append(len(data[data.ajudaMenos == i]))
#explode = [0.1]*len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
#ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
pie = ax2.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.legend(pie[0],labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
#ax2.legend(labels, loc='center right')
ax2.set_title('Quem ajuda menos o Terceiro Setor?')
plt.show()
'''






'''################## ALGORITMO APRIORI (REGRA DE ASSOCIAÇÃO) ###################'''


#data = data.astype(str)
#print (data.head(30))
#print (data.values.tolist())

#association_rules = apriori(data.values.tolist(), min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
#association_results = list(association_rules)
#FONTE: https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/



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

