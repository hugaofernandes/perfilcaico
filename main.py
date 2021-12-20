# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import itertools
from pathlib import Path
from sklearn.cluster import KMeans

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

data['pandemia'] = data['pandemia'].replace(['Muito menos', 'Menos', 'Mesma quantidade', 'Mais', 'Muito mais'],['Reduziu muito as contribuições', 'Reduziu as contribuições', 'Contribui igual', 'Aumentou as contribuições', 'Aumentou muito as contribuições'])
#print (data.pandemia)

data['dinheiro'] = data['dinheiro'].apply(str).str.replace('$ ', '$')
data['dinheiro'] = data['dinheiro'].apply(str).str.replace('$', '\$ ')
#print (data.dinheiro)

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
data.rename(columns={'Centro de Valorização da Vida - CVV':'CVV Caicó'}, inplace=True)


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



'''########################### PERFIL GERAL ##########################'''

from plots import barras, barras2D, barras2D_bairros, barras_avaliacao, barras_bairros, barras_popularidade, clustering3D, pizza2D, pizza2D_ajuda, pizza4D_ajuda, pizza, testeNome, barras_doacoes

pasta = './PERFIL GERAL/'
Path(pasta).mkdir(parents=True, exist_ok=True)
#barras_bairros(data, 'bairro', 'DISTRIBUIÇÃO GERAL POR BAIRROS', pasta)
#pizza(data, 'idade', 'DISTRIBUIÇÃO GERAL POR IDADE', pasta)
#pizza(data, 'fe', 'NÍVEL DE ESPIRITUALIDADE GERAL', pasta)
#pizza(data, 'estadoCivil', 'DISTRIBUIÇÃO GERAL POR ESTADO CIVIL', pasta)
#pizza(data, 'filhos', 'DISTRIBUIÇÃO GERAL POR FILHOS', pasta)
#pizza(data, 'escolaridade', 'DISTRIBUIÇÃO GERAL POR ESCOLARIDADE', pasta)
#pizza(data, 'renda', 'FAIXA DE RENDA DOMICILIAR GERAL', pasta)
#pizza(data, 'ocupacao', 'DISTRIBUIÇÃO GERAL POR OCUPAÇÃO', pasta)
#pizza(data, 'sexo', 'DISTRIBUIÇÃO GERAL POR GÊNERO', pasta)
#pizza(data, 'pandemia', 'EFEITOS DA PANDEMIA NAS CONTRIBUIÇÕES', pasta)
#pizza2D_ajuda(data, 'ajudaMais', 'ajudaMenos', 'QUEM AJUDA MAIS O TERCEITO SETOR?', 'QUEM AJUDA MENOS O TERCEIRO SETOR?', pasta)
#barras(data, ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp'], 'MEIOS DE COMUNICAÇÃO MAIS UTILIZADOS NO GERAL', pasta)
#barras(data, ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], 'MESES PREFERIDOS PARA COLABORAÇÕES NO GERAL', pasta)
#barras(data, ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo'], 'MEIOS PREFERIDOS PARA COLABORAÇÕES NO GERAL', pasta)


'''########################### PERFIL POR INSTITUIÇÕES ##########################'''

def grupos(data, atributo, labels):
    grupoOposto = data
    grupoAlvo = pd.DataFrame()
    for label in labels:
        grupoOposto = grupoOposto[grupoOposto[atributo] != label]
        if label != 'Abstenção':
            grupoAlvo = grupoAlvo.append(data[data[atributo] == label], ignore_index=True)
    return grupoOposto, grupoAlvo

def doadorNice(data, atributos, labels, index):
    test = 0
    for atributo, _labels in zip(atributos, labels):
        for label in _labels:
            ind = data.iloc[[index]]
            if ind[atributo].values[0] != label:
                test += 1
                if test >= 3:
                    return 1
    return 0

def doadorNiceAndBad(data, atributos, labels):
    nice = pd.DataFrame()
    bad = pd.DataFrame()
    for index in range(len(data)):
        ind = doadorNice(data, atributos, labels, index)
        if ind == 0:
            bad = bad.append(data.iloc[[index]], ignore_index=True)
        else:
            nice = nice.append(data.iloc[[index]], ignore_index=True)                
    return nice, bad


def entidades(data, entidade, _pasta):
    bem, ruim = grupos(data, entidade, ['Abstenção', 'Às vezes é Importante', 'Não é Importante', 'Mediana'])
    entidade = testeNome(entidade)
    _pasta = _pasta+entidade+'/'
    Path(_pasta).mkdir(parents=True, exist_ok=True)
    barras2D_bairros(bem, ruim, 'bairro', 'BAIRROS DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'BAIRROS DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)    
    pizza2D(bem, ruim, 'idade', 'FAIXA DE IDADE DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'FAIXA DE IDADE DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'fe', 'NÍVEL DE ESPIRITUALIDADE DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'NÍVEL DE ESPIRITUALIDADE DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'estadoCivil', 'ESTADO CIVIL DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'ESTADO CIVIL DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'filhos', 'RELAÇÃO DE FILHOS DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'RELAÇÃO DE FILHOS DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'escolaridade', 'ESCOLARIDADE DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'ESCOLARIDADE DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'renda', 'RENDA DOMICILIAR DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'RENDA DOMICILIAR DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'ocupacao', 'OCUPAÇÃO DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'OCUPAÇÃO DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'sexo', 'GÊNERO DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'GÊNERO DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp'], 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], 'MESES PREFERIDOS PARA COLABORAÇÃO DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'MESES PREFERIDOS PARA COLABORAÇÃO DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo'], 'MEIOS DE COLABORAÇÃO PREFERIDOS DOS QUE AVALIAM BEM A ENTIDADE:\n'+entidade, 'MEIOS DE COLABORAÇÃO PREFERIDOS DOS QUE AVALIAM RUIM A ENTIDADE:\n'+entidade, _pasta)

pasta = './PERFIL POR INSTITUIÇÃO/'
Path(pasta).mkdir(parents=True, exist_ok=True)
#barras_avaliacao(data, ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro'], ['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'], 'AVALIAÇÃO GERAL DAS ENTIDADES DA REGIÃO', pasta)
#barras_popularidade(data, ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro'], 'POPULARIDADE DAS ENTIDADES DA REGIÃO', pasta)
#entidades(data, 'apae', pasta)
#entidades(data, 'acapam', pasta)
#entidades(data, 'aldeiasSOS', pasta)
#entidades(data, 'abrigo', pasta)
#entidades(data, 'caritas', pasta)
#entidades(data, 'fazendaEsperanca', pasta)
#entidades(data, 'cvv', pasta)
#entidades(data, 'risoterapia', pasta)
#entidades(data, 'hemocentro', pasta)


'''########################### PERFIL POR USUÁRIOS ##########################'''

def usuarios(data, entidade, _pasta):
    bem, ruim = grupos(data, entidade, [0])
    entidade = testeNome(entidade)
    _pasta = _pasta+entidade+'/'
    Path(_pasta).mkdir(parents=True, exist_ok=True)
    barras2D_bairros(bem, ruim, 'bairro', 'BAIRROS DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'BAIRROS DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)    
    pizza2D(bem, ruim, 'idade', 'FAIXA DE IDADE DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'FAIXA DE IDADE DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'fe', 'NÍVEL DE ESPIRITUALIDADE DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'NÍVEL DE ESPIRITUALIDADE DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'estadoCivil', 'ESTADO CIVIL DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'ESTADO CIVIL DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'filhos', 'RELAÇÃO DE FILHOS DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'RELAÇÃO DE FILHOS DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'escolaridade', 'ESCOLARIDADE DOS USUÁRIOS DA ENTIDADE: '+entidade, 'ESCOLARIDADE DOS NÃO USUÁRIOS DA ENTIDADE: '+entidade, _pasta)
    pizza2D(bem, ruim, 'renda', 'RENDA DOMICILIAR DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'RENDA DOMICILIAR DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'ocupacao', 'OCUPAÇÃO DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'OCUPAÇÃO DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    pizza2D(bem, ruim, 'sexo', 'GÊNERO DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'GÊNERO DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp'], 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], 'MESES PREFERIDOS DE COLABORAÇÃO DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'MESES PREFERIDOS DE COLABORAÇÃO DOS NÃO USUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)
    barras2D(bem, ruim, ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo'], 'MEIOS PREFERIDOS DE COLABORAÇÃO DOS USUÁRIOS DA ENTIDADE:\n'+entidade, 'MEIOS PREFERIDOS DE COLABORAÇÃO DOS NÃOUSUÁRIOS DA ENTIDADE:\n'+entidade, _pasta)

pasta = './PERFIL POR USUÁRIO/'
Path(pasta).mkdir(parents=True, exist_ok=True)
#barras(data, ['APAE Caicó', 'Acapam', 'Aldeias Infantis SOS', 'Abrigo Pedro Gurgel', 'Cáritas Diocesana', 'Fazenda da Esperança', 'CVV Caicó', 'Risoterapia', 'Hemocentro Caicó'], 'PROPORÇÃO DE USUÁRIOS POR ENTIDADES', pasta)
#usuarios(data, 'APAE Caicó', pasta)
#usuarios(data, 'Acapam', pasta)
#usuarios(data, 'Aldeias Infantis SOS', pasta)
#usuarios(data, 'Abrigo Pedro Gurgel', pasta)
#usuarios(data, 'Cáritas Diocesana', pasta)
#usuarios(data, 'Fazenda da Esperança', pasta)
#usuarios(data, 'CVV Caicó', pasta)
#usuarios(data, 'Risoterapia', pasta)
#usuarios(data, 'Hemocentro Caicó', pasta)


'''############################# PERFIL POR DOAÇÕES ##################################'''

def doacoes(data, atributo, labels, _pasta):
    bem, ruim = grupos(data, atributo, labels)
    atributo = testeNome(atributo)
    _pasta = _pasta+atributo+'/'
    Path(_pasta).mkdir(parents=True, exist_ok=True)
    barras2D_bairros(bem, ruim, 'bairro', 'BAIRROS DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'BAIRROS DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'idade', 'FAIXA DE IDADE DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'FAIXA DE IDADE DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'fe', 'NÍVEL DE ESPIRITUALIDADE DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'NÍVEL DE ESPIRITUALIDADE DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'estadoCivil', 'ESTADO CIVIL DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'ESTADO CIVIL DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'filhos', 'RELAÇÃO DE FILHOS DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'RELAÇÃO DE FILHOS DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'escolaridade', 'ESCOLARIDADE DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'ESCOLARIDADE DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'renda', 'RENDA DOMICILIAR DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'RENDA DOMICILIAR DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    pizza2D(bem, ruim, 'ocupacao', 'OCUPAÇÃO DOS QUE CONTRIBUEM MAIS COM '+atributo, 'OCUPAÇÃO DOS QUE CONTRIBUEN MENOS COM '+atributo, _pasta)
    pizza2D(bem, ruim, 'sexo', 'GÊNERO DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'GÊNERO DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    barras2D(bem, ruim, ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp'], 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'MEIOS DE COMUNICAÇÃO PREFERIDOS DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)
    barras2D(bem, ruim, ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], 'MESES PREFERIDOS PARA COLABORAÇÃO DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'MESES PREFERIDOS PARA COLABORAÇÃO DOS QUE CONTRIBUE MENOS COM:\n'+atributo, _pasta)
    barras2D(bem, ruim, ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo'], 'MEIOS DE COLABORAÇÃO PREFERIDOS DOS QUE CONTRIBUEM MAIS COM:\n'+atributo, 'MEIOS DE COLABORAÇÃO PREFERIDOS DOS QUE CONTRIBUEM MENOS COM:\n'+atributo, _pasta)

pasta = './PERFIL POR DOAÇÕES/'
Path(pasta).mkdir(parents=True, exist_ok=True)
#barras_doacoes(data, ['dinheiro', 'voluntario', 'alimento', 'roupas', 'higiene', 'racao', 'brinquedos', 'sangue'], 'POPULARIDADE DAS DOAÇÕES', pasta)
#pizza(data, 'dinheiro', 'DOAÇÕES EM DINHEIRO NO ÚLTIMO ANO', pasta)
#pizza(data, 'voluntario', 'TRABALHO VOLUNTÁRIO REALIZADO NO ÚLTIMO ANO', pasta)
#pizza(data, 'alimento', 'DOAÇÕES DE ALIMENTOS NO ÚLTIMO ANO', pasta)
#pizza(data, 'roupas', 'DOAÇÕES DE ROUPAS E AGASALHOS NO ÚLTIMO ANO', pasta)
#pizza(data, 'higiene', 'DOAÇÕES DE PRODUTOS DE LIMPEZA E HIGIENE NO ÚLTIMO ANO', pasta)
#pizza(data, 'racao', 'DOAÇÕES DE RAÇÃO ANIMAL NO ÚLTIMO ANO', pasta)
#pizza(data, 'brinquedos', 'DOAÇÕES DE BRINQUEDOS NO ÚLTIMO ANO', pasta)
#pizza(data, 'sangue', 'DOAÇÕES DE SANGUE NO ÚLTIMO ANO', pasta)
#doacoes(data, 'dinheiro', ['R\\$  0,00 (Zero)', 'Entre R\\$ 1,00 e R\\$ 100,00'], pasta)
#doacoes(data, 'dinheiro', ['R\\$  0,00 (Zero)'], pasta)
#doacoes(data, 'voluntario', ['0 (Zero)'], pasta)
#doacoes(data, 'alimento', ['0 kg (Zero)', 'Entre 1kg e 5 kg'], pasta)
#doacoes(data, 'alimento', ['0 kg (Zero)'], pasta)
#doacoes(data, 'roupas', ['0 (Zero)', 'Entre 1 e 5', 'Entre 6 e 10'], pasta)
#doacoes(data, 'roupas', ['0 (Zero)'], pasta)
#doacoes(data, 'higiene', ['0 (Zero)'], pasta)
#doacoes(data, 'racao', ['0 kg (Zero)'], pasta)
#doacoes(data, 'brinquedos', ['0 (Zero)'], pasta)
#doacoes(data, 'sangue', ['0 (Zero)'], pasta)

#doaMuito, doaPouco = doadorNiceAndBad(data, ['dinheiro', 'voluntario', 'alimento', 'roupas', 'higiene', 'racao', 'brinquedos', 'sangue'], [['R\\$  0,00 (Zero)'], ['0 (Zero)'], ['0 kg (Zero)'], ['0 (Zero)'], ['0 (Zero)'], ['0 kg (Zero)'], ['0 (Zero)'], ['0 (Zero)']])
#barras2D_bairros(doaMuito, doaPouco, 'bairro', 'BAIRROS DOS QUE CONTRIBUEM MAIS', 'BAIRROS DOS QUE CONTRIBUEM MENOS', pasta)


'''################## REGRAS DE ASSOCIAÇÃO ###################'''

#FONTE1: https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/
#FONTE2: https://medium.com/@bernardo.costa/uma-introdu%C3%A7%C3%A3o-ao-algoritmo-apriori-60b11293aa5a

def support(data, atributos, labels): # proporção de X em D
    x = data
    y = len(data)
    for atributo, label in zip(atributos, labels):
        x = x[x[atributo] == label]
        #print (x)
        if len(x) == 0:
            return 0
    return len(x) / y

def confidence(data, atributos, labels): # proporção de X com Y
    x = support(data, atributos[:-1], labels[:-1])
    if x == 0:
        return 0
    x_y = support(data, atributos, labels)
    return  x_y / x

def lift(data, atributos, labels): # lift=1, sem associaçao X_Y; lift>1, association X_Y; lift<1, improvavel X_Y
    y = support(data, atributos[-1:], labels[-1:])
    if y == 0:
        return 0
    x_y = confidence(data, atributos, labels)
    return x_y / y

def conviction(data, atributos, labels): # proporção de X sem Y
    x_y = 1 - confidence(data, atributos, labels)
    if x_y == 0:
        return 0
    y = 1 - support(data, atributos[-1:], labels[-1:])
    return y / x_y

def combineLabels(data, atributos):
    labels = []
    for atributo in atributos:
        labels.append(data[atributo].unique().tolist())
    return list(itertools.product(*labels))

def bestColunas(colunas, atributos):
    newcolunas = colunas
    for atributo in atributos:
        newcolunas.append(atributo)
    return list(set(newcolunas))

def apriori(data, min_suporte=0, min_confianca=0, min_lift=1, min_comprimento=2, max_comprimento=2, pasta='./REGRA DE ASSOCIAÇÃO/', file='apriori_data.csv'):
    colunas = data.columns.tolist()
    pd.DataFrame([['Função', 'Porcentagem', 'Comprimento', 'Atributos', 'Labels']]).to_csv(pasta+file, sep=',', index=False, header=False)
    for comprimento in range(min_comprimento, max_comprimento+1):
        #atributos = list(itertools.combinations(colunas, r=comprimento)) # util para lift
        atributos = list(itertools.permutations(colunas, r=comprimento)) # util para suporte e confiança
        print ('atributos:', len(colunas), 'combinações:', len(atributos), 'comprimento:', comprimento)
        #print ('atributos', colunas)
        colunas = []
        for atributo in atributos:
            labels = combineLabels(data, list(atributo))
            for label in labels:
                
                suporte = support(data, list(atributo), list(label))
                if suporte >= min_suporte:
                    #print ('Support:', suporte, atributo, label)
                    #apriori_data = pd.read_csv(pasta+file, sep=',', header=None)
                    #apriori_data = pd.concat([apriori_data, pd.DataFrame([['Support', suporte, len(atributo), atributo, label]])])
                    #apriori_data.to_csv(pasta+file, sep=',', index=False, header=False)
                    
                    confianca = confidence(data, list(atributo), list(label))
                    if confianca >= min_confianca:
                        #print ('Confidence:', confianca, atributo, label)
                        apriori_data = pd.read_csv(pasta+file, sep=',', header=None)
                        apriori_data = pd.concat([apriori_data, pd.DataFrame([['Confidence', confianca, len(atributo), atributo, label]])])
                        apriori_data.to_csv(pasta+file, sep=',', index=False, header=False)
                        colunas = bestColunas(colunas, atributo)
                
                '''levantamento = lift(data, list(atributo), list(label))
                if levantamento == min_lift:
                    #print ('Lift:', lift, atributo, label)
                    apriori_data = pd.read_csv(pasta+file, sep=',', header=None)
                    apriori_data = pd.concat([apriori_data, pd.DataFrame([['Lift', levantamento, len(atributo), atributo, label]])])
                    apriori_data.to_csv(pasta+file, sep=',', index=False, header=False)
                    colunas = bestColunas(colunas, atributo)'''

pasta = './REGRA DE ASSOCIAÇÃO/'
Path(pasta).mkdir(parents=True, exist_ok=True)
#apriori(data, min_suporte=0.95, min_confianca=0.9, max_comprimento=10)


'''######################## PERFIL POR AGRUPAMENTOS #######################'''

def agrupamento(data, n):
    data['sexo'] = pd.factorize(data['sexo'])[0] #categorização (transformando os dados em inteiros)
    data['idade'] = pd.factorize(data['idade'])[0]
    data['filhos'] = pd.factorize(data['filhos'])[0]
    data['estadoCivil'] = pd.factorize(data['estadoCivil'])[0]
    data['escolaridade'] = pd.factorize(data['escolaridade'])[0]
    data['ocupacao'] = pd.factorize(data['ocupacao'])[0]
    data['bairro'] = pd.factorize(data['bairro'])[0]
    data = data.replace(['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante', 'Abstenção'],[5, 4, 3, 2, 1, 0])
    data['ajudaMais'] = data['ajudaMais'].replace(['Poder Público', 'Iniciativa Privada (Empresas)', 'Sociedade em Geral (Indivíduos)'],[0, 1, 2])
    data['ajudaMenos'] = data['ajudaMenos'].replace(['Poder Público', 'Iniciativa Privada (Empresas)', 'Sociedade em Geral (Indivíduos)'],[0, 1, 2])
    data['dinheiro'] = pd.factorize(data['dinheiro'])[0]
    data['voluntario'] = pd.factorize(data['voluntario'])[0]
    data['alimento'] = pd.factorize(data['alimento'])[0]
    data['roupas'] = pd.factorize(data['roupas'])[0]
    data['higiene'] = pd.factorize(data['higiene'])[0]
    data['racao'] = pd.factorize(data['racao'])[0]
    data['brinquedos'] = pd.factorize(data['brinquedos'])[0]
    data['sangue'] = pd.factorize(data['sangue'])[0]
    data['pandemia'] = pd.factorize(data['pandemia'])[0]
    data['fe'] = pd.factorize(data['fe'])[0]
    data['renda'] = pd.factorize(data['renda'])[0]
    data = (data-data.mean())/data.std() # normalização por desvio padrão
    #data = (data-data.min())/(data.max()-data.min()) # normalização por max e min (entre 0 e 1)
    clustering = KMeans(n_clusters=n)
    clustering.fit(data)
    data['target'] = clustering.labels_
    return data

def perfis(data, labels, _pasta):
    grupoOposto, grupoAlvo = grupos(data, 'target', labels)
    labels = 'GRUPO '+str(labels[0])
    _pasta = _pasta+labels+'/'
    Path(_pasta).mkdir(parents=True, exist_ok=True)
    barras_bairros(grupoAlvo, 'bairro', 'DISTRIBUIÇÃO POR BAIRROS\n'+labels, _pasta)
    pizza(grupoAlvo, 'idade', 'DISTRIBUIÇÃO POR IDADE\n'+labels, _pasta)
    pizza(grupoAlvo, 'fe', 'NÍVEL DE ESPIRITUALIDADE\n'+labels, _pasta)
    pizza(grupoAlvo, 'estadoCivil', 'DISTRIBUIÇÃO POR ESTADO CIVIL\n'+labels, _pasta)
    pizza(grupoAlvo, 'filhos', 'DISTRIBUIÇÃO POR FILHOS\n'+labels, _pasta)
    pizza(grupoAlvo, 'escolaridade', 'DISTRIBUIÇÃO POR ESCOLARIDADE\n'+labels, _pasta)
    pizza(grupoAlvo, 'renda', 'FAIXA DE RENDA DOMICILIAR\n'+labels, _pasta)
    pizza(grupoAlvo, 'ocupacao', 'DISTRIBUIÇÃO POR OCUPAÇÃO\n'+labels, _pasta)
    pizza(grupoAlvo, 'sexo', 'DISTRIBUIÇÃO POR GÊNERO\n'+labels, _pasta)
    pizza2D_ajuda(grupoAlvo, 'ajudaMais', 'ajudaMenos', 'QUEM AJUDA MAIS O TERCEITO SETOR SEGUNDO\n'+labels, 'QUEM AJUDA MENOS O TERCEIRO SETOR SEGUNDO\n'+labels, _pasta)
    barras(grupoAlvo, ['Rádio', 'Blogs e Sites', 'Televisão', 'Jornais e Revistas', 'Carros de Som', 'Igreja', 'Facebook', 'Instagram', 'Whatsapp'], 'MEIOS DE COMUNICAÇÃO MAIS UTILIZADOS\n'+labels, _pasta)
    barras(grupoAlvo, ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'], 'MESES PREFERIDOS PARA COLABORAÇÕES\n'+labels, _pasta)
    barras(grupoAlvo, ['Recolher em casa', 'Transferência ou Depósito', 'Correspondência', 'Pix', 'Troco Solidário', 'Rifas e Sorteios', 'Dízimo'], 'MEIOS PREFERIDOS PARA COLABORAÇÕES\n'+labels, _pasta)
    
    barras_avaliacao(grupoAlvo, ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro'], ['Muito Importante', 'Importante', 'Mediana', 'Às vezes é Importante', 'Não é Importante'], 'AVALIAÇÃO GERAL DAS ENTIDADES DA REGIÃO\n'+labels, _pasta)
    barras_popularidade(grupoAlvo, ['apae', 'acapam', 'aldeiasSOS', 'abrigo', 'caritas', 'fazendaEsperanca', 'cvv', 'risoterapia', 'hemocentro'], 'POPULARIDADE DAS ENTIDADES DA REGIÃO\n'+labels, _pasta)

    barras(grupoAlvo, ['APAE Caicó', 'Acapam', 'Aldeias Infantis SOS', 'Abrigo Pedro Gurgel', 'Cáritas Diocesana', 'Fazenda da Esperança', 'CVV Caicó', 'Risoterapia', 'Hemocentro Caicó'], 'PROPORÇÃO DE USUÁRIOS POR ENTIDADES\n'+labels, _pasta)

    barras_doacoes(grupoAlvo, ['dinheiro', 'voluntario', 'alimento', 'roupas', 'higiene', 'racao', 'brinquedos', 'sangue'], 'POPULARIDADE DAS DOAÇÕES\n'+labels, _pasta)
    pizza(grupoAlvo, 'dinheiro', 'DOAÇÕES EM DINHEIRO NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'voluntario', 'TRABALHO VOLUNTÁRIO REALIZADO NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'alimento', 'DOAÇÕES DE ALIMENTOS NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'roupas', 'DOAÇÕES DE ROUPAS E AGASALHOS NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'higiene', 'DOAÇÕES DE PRODUTOS DE LIMPEZA E HIGIENE NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'racao', 'DOAÇÕES DE RAÇÃO ANIMAL NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'brinquedos', 'DOAÇÕES DE BRINQUEDOS NO ÚLTIMO ANO\n'+labels, _pasta)
    pizza(grupoAlvo, 'sangue', 'DOAÇÕES DE SANGUE NO ÚLTIMO ANO\n'+labels, _pasta)

    #apriori(grupoAlvo.loc[:, data.columns != 'target'], min_suporte=0.95, max_comprimento=10, pasta=_pasta, file='apriori_data ('+labels+').csv')


pasta = './PERFIL POR AGRUPAMENTO/'
Path(pasta).mkdir(parents=True, exist_ok=True)

#data.to_csv(pasta+'dataset_processed.csv', sep=',', index=False)
#data_clustering = agrupamento(data, 4)
#data_clustering.to_csv(pasta+'dataset_clustering.csv', sep=',', index=False)

#data_clustering = pd.read_csv(pasta+'dataset_clustering.csv', sep=',')
#clustering3D(data_clustering)


#data = pd.read_csv(pasta+'dataset_processed.csv', sep=',')
#data_clustering = pd.read_csv(pasta+'dataset_clustering.csv', sep=',')
#data['target'] = data_clustering['target']

#perfis(data, [0], pasta)
#perfis(data, [1], pasta)
#perfis(data, [2], pasta)
#perfis(data, [3], pasta)

