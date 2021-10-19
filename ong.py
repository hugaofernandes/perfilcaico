
import numpy as np
import pandas as pd

data = pd.read_csv('./Downloads/censo2010.csv', sep=';')
data.columns = ['codigo', 'zona', 'logradouro', 'numero', 'complemento', 'latitude', 'longitude', 'localidade', 'referencia', 'especie', 'tipo', 'indicador', 'identificacao', 'quadra', 'fase', 'cep']

pd.set_option('display.max_rows', None)
#print (data.codigo.value_counts())

#bairros = data.localidade.value_counts()
print (data.localidade.value_counts())
#bairros.to_csv('bairros.csv', sep=';')

#centro = data[data.localidade == 'CENTRO']
#print (centro.codigo.value_counts())

#alto = data[data.localidade == 'RECREIO']
#print (alto.codigo.value_counts())

#print (data.zona.value_counts())
'''
#print (data.codigo.unique())
setores = data.codigo.unique()
for i in setores:
    setor = data[data.codigo == i]
    print ()
    print (i, setor.zona.unique().item())
    print (setor.localidade.value_counts())
'''



