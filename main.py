# -*- coding: utf-8 -*-

from plotsDescritivos import idades, comunicacao
from tratamento import colunasNome, testeColunasNome, excluirColuna, testeExcluirColuna, notasToInt, testeNotasToInt, binarizacao, testeBinarizacao, testeToTexto, toTexto
import pandas as pd
import numpy as np

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #remover msg warnings
pd.set_option('display.max_rows', None) # mostrar prints completos

data = pd.read_csv('./dataset.csv', sep=',') #abrindo o arquivo dataset.csv e separando por virgula

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
ANALISES DESCRITIVAS:
            mostrar as idades
mostrar os bairros
estado civil e filhos
escolaridade
espiritualidade
notas e taxa de popularidade
    apae
    acapam
    abrigo pedro gurgel
    aldeias SOS
    casa da caridade
    caritas
    fazenda da esperança
    CVV
    risoterapia
    hemocentro
já precisou de ajuda?
quem doa mais e menos
meios de comunicação e taxa de popularidade
dizimo
dinheiro
ração
alimento
roupas
voluntario
higiene e limpeza
brinquedos
sangue
preferencias e taxa de popularidade
meses e taxa de popularidade
comparação com antes da pandemia
ocupação
renda

ANALISES INFERENCIAIS:
agrupamento
associação
'''

